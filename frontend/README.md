# amigda university frontend

Frontend for the Multi-Agent Student Services Assistant built with Next.js.

## features

- modern university landing page
- floating ai student assistant
- responsive design
- announcements section
- student services section
- chatbot integrated with the backend api
- fullscreen chatbot support

## tech stack

- next.js
- react
- tailwind css
- typescript

## getting started

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open:

```
http://localhost:3000
```

## backend configuration

The frontend communicates with the backend API using the following environment variable:

```
NEXT_PUBLIC_API_URL
```

### local development

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

### cloud run

```
NEXT_PUBLIC_API_URL=https://student-services-backend-381407246613.asia-southeast1.run.app
```

## deployment

Production deployments use:

- frontend: Google Cloud Run
- backend: Google Cloud Run
- database: Google Cloud SQL (PostgreSQL)

The frontend communicates with the deployed backend through the `NEXT_PUBLIC_API_URL` environment variable.

## project structure

```
src/
├── app/
├── components/
│   ├── Announcements.tsx
│   ├── Hero.tsx
│   ├── Navbar.tsx
│   ├── StudentAssistant.tsx
│   └── StudentServices.tsx
```

## notes

This frontend is part of the Multi-Agent Student Services Assistant internship project developed for Amigda Labs.