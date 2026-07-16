export default function Hero() {
  return (
    <section className="relative flex min-h-screen items-center overflow-hidden px-6 pt-28">
      <div className="absolute inset-0">
        <div className="absolute -left-[20%] top-[10%] h-[700px] w-[700px] rounded-full bg-white/10 blur-[180px]" />
        <div className="absolute -right-[10%] bottom-[-20%] h-[700px] w-[700px] rounded-full bg-[#ff6961]/15 blur-[180px]" />
      </div>

      <div className="relative z-10 mx-auto w-full max-w-7xl">
        <div className="max-w-5xl">
          <p className="mb-6 text-sm font-medium uppercase tracking-[0.3em] text-[#ff6961]">
            Learn. Build. Shape the future.
          </p>

          <h1 className="text-5xl font-semibold leading-[0.95] tracking-[-0.05em] text-white sm:text-7xl lg:text-[110px]">
            Education for the
            <span className="block text-white/35">AI-driven world.</span>
          </h1>

          <p className="mt-8 max-w-2xl text-base leading-8 text-white/50 md:text-lg">
            Amigda University is a fictional digital campus built to demonstrate
            intelligent student services powered by multi-agent AI.
          </p>

          <div className="mt-10 flex flex-wrap gap-4">
            <a
              href="#services"
              className="rounded-full bg-[#ff6961] px-7 py-4 text-sm font-medium text-black transition hover:bg-[#ff7b74]"
            >
              Explore student services
            </a>

            <a
              href="#about"
              className="rounded-full border border-white/15 px-7 py-4 text-sm font-medium text-white transition hover:bg-white/10"
            >
              Discover the university
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}