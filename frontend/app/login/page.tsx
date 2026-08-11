import LoginForm from "@/components/auth/LoginForm";

export default function LoginPage() {
  return (
    <main className="relative flex min-h-screen items-center justify-center overflow-hidden bg-[#020617] px-6 py-12">
      <div className="absolute -left-40 -top-40 h-96 w-96 rounded-full bg-violet-700/20 blur-[120px]" />
      <div className="absolute -bottom-40 -right-40 h-96 w-96 rounded-full bg-purple-700/20 blur-[120px]" />

      <div className="relative w-full max-w-md">
        <LoginForm />
      </div>
    </main>
  );
}