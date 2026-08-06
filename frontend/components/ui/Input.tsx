"use client";

import { InputHTMLAttributes } from "react";

import clsx from "clsx";

interface InputProps
    extends InputHTMLAttributes<HTMLInputElement> {

    label?: string;

    error?: string;

}

export default function Input({

    label,

    error,

    className,

    ...props

}: InputProps) {

    return (

        <div className="space-y-2">

            {

                label && (

                    <label
                        className="block text-sm font-medium text-gray-700"
                    >

                        {label}

                    </label>

                )

            }

            <input

                className={clsx(

                    "w-full rounded-lg border border-gray-300 px-4 py-2",

                    "outline-none transition",

                    "focus:border-blue-500",

                    "focus:ring-2 focus:ring-blue-200",

                    error &&
                        "border-red-500",

                    className,

                )}

                {...props}

            />

            {

                error && (

                    <p
                        className="text-sm text-red-500"
                    >

                        {error}

                    </p>

                )

            }

        </div>

    );

}