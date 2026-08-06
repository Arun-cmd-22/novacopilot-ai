import { z } from "zod";

export const loginSchema = z.object({

    username: z.string()
        .min(
            3,
            "Username must contain at least 3 characters.",
        ),

    password: z
        .string()
        .min(
            8,
            "Password must contain at least 8 characters.",
        ),

});

export type LoginFormData =
    z.infer<typeof loginSchema>;

export const registerSchema = z.object({

    username: z
        .string()
        .min(
            3,
            "Username must contain at least 3 characters.",
        ),

    email: z
        .email(
            "Invalid email address.",
        ),

    password: z
        .string()
        .min(
            8,
            "Password must contain at least 8 characters.",
        ),

    confirmPassword: z
        .string(),

}).refine(

    (data) =>
        data.password ===
        data.confirmPassword,

    {

        message:
            "Passwords do not match.",

        path: ["confirmPassword"],

    },

);

export type RegisterFormData =
    z.infer<typeof registerSchema>;