const services = [
  {
    number: "01",
    title: "Billing & Tuition",
    description:
      "Review tuition balances and get assistance with billing-related concerns.",
  },
  {
    number: "02",
    title: "Class Schedules",
    description:
      "Access class schedules, academic times, and important student deadlines.",
  },
  {
    number: "03",
    title: "Enrollment",
    description:
      "Find guidance for enrollment and other academic service concerns.",
  },
  {
    number: "04",
    title: "Student Support",
    description:
      "Get assistance or escalate unresolved concerns to student support.",
  },
];

export default function StudentServices() {
  return (
    <section id="services" className="px-6 py-28">
      <div className="mx-auto max-w-7xl">
        <div className="mb-16 max-w-3xl">
          <p className="mb-4 text-sm uppercase tracking-[0.3em] text-[#ff6961]">
            Student Services
          </p>

          <h2 className="text-4xl font-semibold tracking-[-0.04em] text-white md:text-6xl">
            Support built around
            <span className="block text-white/35">the student experience.</span>
          </h2>
        </div>

        <div className="grid border-t border-white/10 md:grid-cols-2">
          {services.map((service) => (
            <article
              key={service.number}
              className="group border-b border-white/10 p-8 transition hover:bg-white/[0.04] md:p-12 md:odd:border-r"
            >
              <div className="flex items-start justify-between gap-6">
                <div>
                  <span className="text-xs text-[#ff6961]">
                    {service.number}
                  </span>

                  <h3 className="mt-8 text-2xl font-medium tracking-tight text-white md:text-3xl">
                    {service.title}
                  </h3>

                  <p className="mt-4 max-w-md leading-7 text-white/45">
                    {service.description}
                  </p>
                </div>

                <span className="text-2xl text-white/20 transition group-hover:text-[#ff6961]">
                  ↗
                </span>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}