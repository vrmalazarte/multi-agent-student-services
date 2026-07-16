"use client";

import { useState } from "react";

type Message = {
  role: "user" | "assistant";
  content: string;
};

type ChatResponse = {
  answer: string;
  category: "general" | "billing" | "schedule" | "escalation";
  handled_by_agent: string;
  handoff_reason: string | null;
  action_items: string[];
  memory_updates: {
    key: string;
    value: string;
  }[];
  needs_human: boolean;
  thread_id: number;
};

export default function StudentAssistant() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [threadId, setThreadId] = useState<number | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  async function handleSend() {
    if (!input.trim() || isLoading) {
      return;
    }

    const userMessage: Message = {
      role: "user",
      content: input,
    };

    setMessages((currentMessages) => [
      ...currentMessages,
      userMessage,
    ]);

    setInput("");
    setIsLoading(true);

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/chat`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: userMessage.content,
            thread_id: threadId,
          }),
        },
      );

      if (!response.ok) {
        throw new Error("Failed to send message");
      }

      const data: ChatResponse = await response.json();

      setThreadId(data.thread_id);

      const assistantMessage: Message = {
        role: "assistant",
        content: data.answer,
      };

      setMessages((currentMessages) => [
        ...currentMessages,
        assistantMessage,
      ]);
    } catch (error) {
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  }

  if (!isOpen) {
    return (
      <button
        type="button"
        onClick={() => setIsOpen(true)}
        className="fixed bottom-6 right-6 z-50 flex h-16 w-16 items-center justify-center rounded-full border border-white/15 bg-[#ff6961] text-2xl text-black shadow-2xl transition hover:scale-105"
        aria-label="Open student assistant"
      >
        ✦
      </button>
    );
  }

  return (
    <div
      className={`fixed z-50 ${
        isFullscreen
          ? "inset-0 bg-[#080b10]/95 p-4 md:p-8"
          : "bottom-6 right-6 h-[650px] w-[calc(100%-3rem)] max-w-[460px]"
      }`}
    >
      <div className="flex h-full w-full flex-col overflow-hidden rounded-[20px] border border-white/15 bg-[#9bb8cf] text-[#29266d] shadow-2xl">
        <header className="flex h-[58px] shrink-0 items-center justify-between px-5">
          <p className="text-sm font-semibold">
            Amigda University
          </p>

          <div className="flex items-center gap-1">
            <button
              type="button"
              onClick={() =>
                setIsFullscreen((current) => !current)
              }
              className="flex h-9 w-9 items-center justify-center rounded-md transition hover:bg-black/10"
              aria-label="Toggle fullscreen"
            >
              {isFullscreen ? "↙" : "↗"}
            </button>

            <button
              type="button"
              onClick={() => {
                setIsFullscreen(false);
                setIsOpen(false);
              }}
              className="flex h-9 w-9 items-center justify-center rounded-md text-xl transition hover:bg-black/10"
              aria-label="Close student assistant"
            >
              ×
            </button>
          </div>
        </header>

        <main className="flex flex-1 overflow-y-auto px-5">
          {messages.length === 0 ? (
            <div className="flex h-full w-full items-center justify-center">
              <h2 className="max-w-lg text-center text-xl font-semibold md:text-2xl">
                Hi there! Welcome to Amigda University! How can I help you?
              </h2>
            </div>
          ) : (
            <div className="flex w-full flex-col gap-3 py-5">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`flex ${
                    message.role === "user"
                      ? "justify-end"
                      : "justify-start"
                  }`}
                >
                  <div
                    className={`max-w-[80%] rounded-[18px] px-4 py-3 text-sm leading-6 ${
                      message.role === "user"
                        ? "bg-[#f2d8d9]"
                        : "bg-white/70"
                    }`}
                  >
                    {message.content}
                  </div>
                </div>
              ))}

              {isLoading && (
                <div className="flex justify-start">
                  <div className="rounded-[18px] bg-white/60 px-4 py-3 text-sm">
                    Thinking...
                  </div>
                </div>
              )}
            </div>
          )}
        </main>

        <footer className="shrink-0 p-4">
          <div className="rounded-[26px] bg-[#f2d8d9] px-5 py-4">
            <input
              type="text"
              value={input}
              onChange={(event) =>
                setInput(event.target.value)
              }
              onKeyDown={(event) => {
                if (event.key === "Enter") {
                  handleSend();
                }
              }}
              placeholder="Ask Amigda University Assistant"
              className="h-10 w-full bg-transparent text-[#29266d] outline-none placeholder:text-[#4f4a9a]/70"
            />

            <div className="mt-3 flex items-center justify-end">
              <button
                type="button"
                onClick={handleSend}
                disabled={isLoading}
                className="flex h-11 w-11 items-center justify-center rounded-full bg-[#bd6668] text-lg text-white transition hover:scale-105 disabled:cursor-not-allowed disabled:opacity-50"
                aria-label="Send message"
              >
                ↑
              </button>
            </div>
          </div>
        </footer>
      </div>
    </div>
  );
}