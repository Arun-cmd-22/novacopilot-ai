import json

import httpx

from fastapi import HTTPException


class OllamaService:

    # ==========================================================
    # GET INSTALLED MODELS
    # ==========================================================

    @staticmethod
    def get_installed_models(
        base_url: str,
    ):

        try:

            response = httpx.get(
                f"{base_url.rstrip('/')}/api/tags",
                timeout=30,
            )

            response.raise_for_status()

            return response.json()

        except httpx.RequestError as e:

            raise HTTPException(
                status_code=503,
                detail=f"Unable to connect to Ollama: {str(e)}",
            )

        except httpx.HTTPStatusError as e:

            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.text,
            )

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )

    # ==========================================================
    # NORMAL CHAT
    # ==========================================================

    @staticmethod
    def chat(
        base_url: str,
        model: str,
        messages: list,
    ):

        try:

            response = httpx.post(
                f"{base_url.rstrip('/')}/api/chat",

                json={
                    "model": model,
                    "messages": messages,
                    "stream": False,

                    # Keep model loaded
                    "keep_alive": "10m",

                    # Faster responses
                    "options": {
                        "temperature": 0.2,
                        "num_predict": 512,
                    },
                },

                timeout=300,
            )

            response.raise_for_status()

            return response.json()

        except httpx.ConnectError:

            raise HTTPException(
                status_code=503,
                detail=(
                    "Unable to connect to Ollama. "
                    "Make sure Ollama is running on "
                    "http://127.0.0.1:11434"
                ),
            )

        except httpx.TimeoutException:

            raise HTTPException(
                status_code=504,
                detail="Ollama request timed out.",
            )

        except httpx.HTTPStatusError as e:

            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.text,
            )

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )

    # ==========================================================
    # STREAMING CHAT
    # ==========================================================

    @staticmethod
    def chat_stream(
        base_url: str,
        model: str,
        messages: list,
    ):

        try:

            with httpx.stream(
                "POST",
                f"{base_url.rstrip('/')}/api/chat",

                json={
                    "model": model,
                    "messages": messages,
                    "stream": True,

                    # Keep Qwen loaded
                    "keep_alive": "10m",

                    # Faster generation
                    "options": {
                        "temperature": 0.2,
                        "num_predict": 512,
                    },
                },

                timeout=None,

            ) as response:

                response.raise_for_status()

                for line in response.iter_lines():

                    if not line:
                        continue

                    try:

                        data = json.loads(line)

                        message_data = data.get(
                            "message",
                            {},
                        )

                        content = message_data.get(
                            "content",
                            "",
                        )

                        if content:
                            yield content

                        # Ollama sends done=true
                        if data.get("done") is True:
                            break

                    except json.JSONDecodeError:

                        continue

        except httpx.ConnectError:

            raise HTTPException(
                status_code=503,
                detail=(
                    "Unable to connect to Ollama. "
                    "Make sure Ollama is running on "
                    "http://127.0.0.1:11434"
                ),
            )

        except httpx.TimeoutException:

            raise HTTPException(
                status_code=504,
                detail="Ollama streaming request timed out.",
            )

        except httpx.HTTPStatusError as e:

            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.text,
            )

        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=str(e),
            )