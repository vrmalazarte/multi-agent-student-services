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

export default function Home() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [threadId, setThreadId] = useState<number | null>(null);
  const [isLoading, setIsLoading] = useState(false);

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

  return (
    <main className="relative flex min-h-screen items-center justify-center overflow-hidden bg-black p-6 text-white">
    {/* Abstract blurred background */}
    <div className="absolute inset-0">
      <div className="absolute -left-[15%] top-[5%] h-[75%] w-[70%] rounded-full bg-gray-500/70 blur-[150px]" />

      <div className="absolute -bottom-[30%] left-[5%] h-[85%] w-[80%] rounded-full bg-black/90 blur-[140px]" />

      <div className="absolute -right-[20%] top-[10%] h-[70%] w-[55%] rounded-full bg-gray-500/80 blur-[130px]" />

      <div className="absolute right-[5%] top-[15%] h-[55%] w-[45%] rounded-full bg-black blur-[100px]" />

      <div className="absolute inset-0 bg-black/20" />
    </div>

    {/* Medium fine grain overlay */}
    <div
      className="pointer-events-none absolute inset-0 z-[1] opacity-[0.16]"
      style={{
        backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 110 110' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.25' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.65'/%3E%3C/svg%3E")`,
        backgroundSize: "110px 110px",
      }}
    />

      <div className="relative z-10 flex h-[700px] w-full max-w-3xl flex-col overflow-hidden rounded-[32px] border border-white/15 bg-black/25 shadow-2xl backdrop-blur-3xl">
        <header className="border-b border-white/10 p-6">
          <h1 className="text-xl font-semibold tracking-tight">
            Student Services Assistant
          </h1>

          <p className="mt-1 text-sm text-white/50">
            Ask about billing, schedules, or student support.
          </p>
        </header>

        <section className="flex-1 overflow-y-auto p-6">
          {messages.length === 0 ? (
            <div className="flex h-full items-center justify-center">
              <div className="text-center">
                <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full border border-white/10 bg-white/10 backdrop-blur-xl">
                  ✦
                </div>

                <p className="font-medium text-white/90">
                  Start a conversation with the assistant.
                </p>

                <p className="mt-2 text-sm text-white/40">
                  I can help with billing, schedules, and student support.
                </p>
              </div>
            </div>
          ) : (
            <div className="flex flex-col gap-3">
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
                    className={`max-w-[75%] rounded-[22px] px-4 py-3 text-sm ${
                      message.role === "user"
                        ? "bg-white text-black"
                        : "border border-white/10 bg-white/[0.08] text-white"
                    }`}
                  >
                    {message.content}
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <footer className="border-t border-white/10 p-4">
          <div className="flex items-center gap-3">
            <div className="flex flex-1 items-center rounded-full border border-white/10 bg-white/[0.08] backdrop-blur-2xl">
              <input
                type="text"
                value={input}
                onChange={(event) => setInput(event.target.value)}
                onKeyDown={(event) => {
                  if (event.key === "Enter") {
                    handleSend();
                  }
                }}
                placeholder="Type your message..."
                className="h-14 w-full bg-transparent px-6 text-white outline-none placeholder:text-white/30"
              />
            </div>

            <button
            onClick={handleSend}
            className="flex h-14 w-14 shrink-0 items-center justify-center rounded-full bg-white text-lg text-black transition hover:bg-white/80">
              ↑
            </button>
          </div>
        </footer>
      </div>
    </main>
  );
}