interface SpinnerProps {

    size?: number;

}

export default function Spinner({

    size = 20,

}: SpinnerProps) {

    return (

        <svg

            className="animate-spin"

            width={size}

            height={size}

            viewBox="0 0 24 24"

            fill="none"

            xmlns="http://www.w3.org/2000/svg"

            role="status"

            aria-label="Loading"

        >

            <circle

                cx="12"

                cy="12"

                r="10"

                stroke="currentColor"

                strokeWidth="4"

                opacity="0.25"

            />

            <path

                d="M22 12a10 10 0 00-10-10"

                stroke="currentColor"

                strokeWidth="4"

                strokeLinecap="round"

            />

        </svg>

    );

}