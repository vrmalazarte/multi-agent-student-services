const announcements = [
  {
    date: "July 14, 2026",
    category: "Academic",
    title: "First semester enrollment reminders",
  },
  {
    date: "July 10, 2026",
    category: "Student Services",
    title: "Updated student support request process",
  },
  {
    date: "July 6, 2026",
    category: "Campus",
    title: "AI student assistant now available",
  },
];

export default function Announcements() {
  return (
    <section id="announcements" className="px-6 py-28">
      <div className="mx-auto max-w-7xl">
        <div className="mb-16 flex flex-col justify-between gap-6 md:flex-row md:items-end">
          <div>
            <p className="mb-4 text-sm uppercase tracking-[0.3em] text-[#ff6961]">
              Campus Updates
            </p>

            <h2 className="text-4xl font-semibold tracking-[-0.04em] text-white md:text-6xl">
              Latest announcements.
            </h2>
          </div>

          <p className="max-w-md leading-7 text-white/45">
            Stay informed about academic services, campus updates, and student
            support.
          </p>
        </div>

        <div className="border-t border-white/10">
          {announcements.map((announcement) => (
            <article
              key={announcement.title}
              className="group grid gap-5 border-b border-white/10 py-8 transition md:grid-cols-[180px_180px_1fr] md:items-center"
            >
              <p className="text-sm text-white/35">{announcement.date}</p>

              <p className="text-sm text-[#ff6961]">
                {announcement.category}
              </p>

              <h3 className="text-xl font-medium text-white transition group-hover:translate-x-2 md:text-2xl">
                {announcement.title}
              </h3>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}