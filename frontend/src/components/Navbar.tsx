import Image from "next/image";

export default function Navbar() {
  return (
    <header className="fixed left-0 top-6 z-40 w-full px-4 sm:px-6">
     <nav className="mx-auto flex h-14 w-full max-w-5xl items-center justify-between rounded-md border border-white/15 bg-white/5 px-4 shadow-2xl backdrop-blur-xl sm:px-6">
        <a href="#" className="flex items-center gap-3">
          <div className="relative h-10 w-10 shrink-0">
            <Image
              src="/assets/amigda-logo.png"
              alt="Amigda University Logo"
              fill
              sizes="40px"
              priority
              className="object-contain"
            />
          </div>
          
          <div>
            <p className="text-sm font-semibold tracking-tight text-white">
              AMIGDA
            </p>
            <p className="text-[10px] tracking-[0.2em] text-white/40">
              UNIVERSITY
            </p>
          </div>
        </a>

        <div className="hidden items-center gap-8 text-sm text-white/60 md:flex">
          <a href="#services" className="transition hover:text-white">
            Student Services
          </a>

          <a href="#announcements" className="transition hover:text-white">
            Announcements
          </a>

          <a href="#about" className="transition hover:text-white">
            About
          </a>
        </div>

        <span className="rounded-full border border-white/10 px-4 py-2 text-xs text-white/50">
          Student Portal
        </span>
      </nav>
    </header>
  );
}