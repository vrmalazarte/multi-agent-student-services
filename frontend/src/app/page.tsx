import Announcements from "@/components/Announcements";
import Hero from "@/components/Hero";
import Navbar from "@/components/Navbar";
import StudentAssistant from "@/components/StudentAssistant";
import StudentServices from "@/components/StudentServices";

export default function Home() {
  return (
    <main className="min-h-screen overflow-hidden bg-[#080b10] text-white">
      <Navbar />

      <Hero />

      <StudentServices />

      <Announcements />

      <section id="about" className="px-6 py-28">
        <div className="mx-auto max-w-7xl border-t border-white/10 pt-20">
          <p className="text-sm uppercase tracking-[0.3em] text-[#ff6961]">
            Amigda University
          </p>

          <div className="mt-8 grid gap-10 md:grid-cols-2">
            <h2 className="text-4xl font-semibold tracking-[-0.04em] md:text-6xl">
              A fictional Philippine digital campus for intelligent student
              services.
            </h2>

            <p className="max-w-xl leading-8 text-white/45">
              This university interface was created as a demonstration of a
              multi-agent AI student services system. The assistant supports
              tuition concerns, class schedules, academic deadlines, and student
              support requests.
            </p>
          </div>
        </div>
      </section>

      <StudentAssistant />
    </main>
  );
}