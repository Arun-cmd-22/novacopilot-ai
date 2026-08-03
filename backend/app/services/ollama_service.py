import json

import httpx

from fastapi import HTTPException


class OllamaService:

    @staticmethod
    def get_installed_models(
        base_url: str,
    ):

        try:

            response = httpx.get(
                f"{base_url}/api/tags",
                timeout=30,
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )

    @staticmethod
    def chat(
        base_url: str,
        model: str,
        messages: list,
    ):

        try:

            response = httpx.post(
                f"{base_url}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": False,
                },
                timeout=300,
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )

    @staticmethod
    def chat_stream(
        base_url: str,
        model: str,
        messages: list,
    ):

        try:

            with httpx.stream(
                "POST",
                f"{base_url}/api/chat",
                json={
                    "model": model,
                    "messages": messages,
                    "stream": True,
                },
                timeout=None,
            ) as response:

                response.raise_for_status()

                for line in response.iter_lines():

                    if not line:
                        continue

                    try:

                        data = json.loads(line)

                        if "message" in data:

                            yield data["message"]["content"]

                    except Exception:
                        continue

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )