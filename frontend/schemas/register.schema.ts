import { z } from "zod";

export const registerSchema = z.object({
  full_name: z
    .string()
    .trim()
    .min(2, "Full name must be at least 2 characters")
    .max(150, "Full name must not exceed 150 characters")
    .regex(
      /^[A-Za-z]+(?: [A-Za-z]+)*$/,
      "Full name can contain only letters and spaces",
    ),

  email: z
    .string()
    .trim()
    .email("Enter a valid email address"),

  mobile: z
    .string()
    .trim()
    .regex(
      /^\+?[1-9]\d{7,14}$/,
      "Enter a valid mobile number",
    ),

  password: z
    .string()
    .min(8, "Password must be at least 8 characters"),
});

export type RegisterFormData = z.infer<typeof registerSchema>;