"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Mail, Sparkles } from "lucide-react";

import AuthService from "@/services/auth.service";
import { useAuthStore } from "@/store/auth.store";
import Input from "@/components/ui/Input";
import PasswordInput from "@/components/ui/PasswordInput";
import Button from "@/components/ui/Button";
import Card from "@/components/ui/Card";
import { loginSchema, type LoginFormData } from "@/schemas/auth.schema";

export default function LoginForm() {
  const router = useRouter();
  const setAuth = useAuthStore((state) => state.setAuth);
  const [serverError, setServerError] = useState("");

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: "",
      password: "",
      rememberMe: false,
    },
  });

  const onSubmit = async (data: LoginFormData) => {
    setServerError("");

    try {
      const response = await AuthService.login({
        email: data.email,
        password: data.password,
      });

      if (!response.success) {
        setServerError(response.message);
        return;
      }

      setAuth(
        response.user,
        response.access_token,
        response.refresh_token,
      );

      router.push("/dashboard");
    } catch {
      setServerError("Unable to connect to the server.");
    }
  };

  return (
    <Card>
      <div className="mb-8 text-center">
        <div className="mx-auto mb-5 flex h-16 w-16 items-center justify-center rounded-2xl bg-violet-600/20 text-violet-400">
          <Sparkles size={28} />
        </div>

        <h1 className="text-3xl font-bold text-white">
          Welcome back
        </h1>

        <p className="mt-2 text-sm text-slate-400">
          Sign in to your NovaCopilot workspace
        </p>
      </div>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
        <div>
          <Input
            {...register("email")}
            label="Email"
            type="email"
            icon={Mail}
            placeholder="Enter your email"
          />

          {errors.email && (
            <p className="mt-1 text-xs text-red-400">
              {errors.email.message}
            </p>
          )}
        </div>

        <div>
          <PasswordInput
            {...register("password")}
            label="Password"
            placeholder="Enter your password"
          />

          {errors.password && (
            <p className="mt-1 text-xs text-red-400">
              {errors.password.message}
            </p>
          )}
        </div>

        <div className="flex items-center justify-between">
          <label className="flex cursor-pointer items-center gap-2 text-sm text-slate-400">
            <input
              type="checkbox"
              {...register("rememberMe")}
              className="h-4 w-4 accent-violet-600"
            />
            Remember me
          </label>

          <button
            type="button"
            onClick={() => router.push("/forgot-password")}
            className="text-sm text-violet-400 hover:text-violet-300"
          >
            Forgot password?
          </button>
        </div>

        {serverError && (
          <div className="rounded-xl border border-red-500/20 bg-red-500/10 p-3 text-sm text-red-400">
            {serverError}
          </div>
        )}

        <Button type="submit" loading={isSubmitting}>
          Sign in
        </Button>
      </form>

      <p className="mt-6 text-center text-sm text-slate-500">
        Don't have an account?{" "}
        <button
          type="button"
          onClick={() => router.push("/register")}
          className="font-medium text-violet-400 hover:text-violet-300"
        >
          Register
        </button>
      </p>
    </Card>
  );
}