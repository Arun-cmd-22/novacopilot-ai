import { ReactNode } from "react";

import clsx from "clsx";

interface CardProps {

    children: ReactNode;

    className?: string;

}

export default function Card({

    children,

    className,

}: CardProps) {

    return (

        <div

            className={clsx(

                "rounded-xl",

                "bg-white",

                "shadow-md",

                "border",

                "border-gray-200",

                "p-6",

                className,

            )}

        >

            {children}

        </div>

    );

}