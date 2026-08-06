"use client";

import { ButtonHTMLAttributes } from "react";

import clsx from "clsx";

interface ButtonProps
    extends ButtonHTMLAttributes<HTMLButtonElement> {

    loading?: boolean;

    variant?:
        | "primary"
        | "secondary"
        | "danger";

}

export default function Button({

    children,

    loading = false,

    variant = "primary",

    className,

    disabled,

    ...props

}: ButtonProps) {

    return (

        <button

            className={clsx(

                "w-full rounded-lg px-4 py-2 font-medium transition",

                {

                    "bg-blue-600 text-white hover:bg-blue-700":
                        variant === "primary",

                    "bg-gray-600 text-white hover:bg-gray-700":
                        variant === "secondary",

                    "bg-red-600 text-white hover:bg-red-700":
                        variant === "danger",

                },

                className,

            )}

            disabled={disabled || loading}

            {...props}

        >

            {loading
                ? "Loading..."
                : children}

        </button>

    );

}