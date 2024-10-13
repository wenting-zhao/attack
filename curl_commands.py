
#just hits the endpoint
CURL_COMMAND_1 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[],\"event_data\":null,\"fn_index\":38,\"trigger_id\":79,\"session_hash\":\"{{SESSION_ID}}\"}'"


#not sure if this one is needed
CURL_COMMAND_2 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[{\"text\":\"\",\"files\":[]}],\"event_data\":null,\"fn_index\":39,\"trigger_id\":79,\"session_hash\":\"{{SESSION_ID}}\"}'"

#hits api with instruction
CURL_COMMAND_3 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[null,null,\"\",\"\",{\"text\":\"{{INSTRUCTION}}\",\"files\":[]},{\"text_models\":[\"chatgpt-4o-latest-20240903\",\"gpt-4o-mini-2024-07-18\",\"gpt-4o-2024-08-06\",\"gpt-4o-2024-05-13\",\"grok-2-2024-08-13\",\"grok-2-mini-2024-08-13\",\"claude-3-5-sonnet-20240620\",\"llama-3.2-vision-90b-instruct\",\"llama-3.2-vision-11b-instruct\",\"llama-3.2-3b-instruct\",\"llama-3.2-1b-instruct\",\"llama-3.1-405b-instruct-bf16\",\"llama-3.1-405b-instruct-fp8\",\"llama-3.1-70b-instruct\",\"llama-3.1-8b-instruct\",\"gemini-1.5-pro-exp-0827\",\"gemini-1.5-flash-exp-0827\",\"gemini-1.5-flash-8b-exp-0827\",\"gemini-1.5-pro-api-0514\",\"gemini-1.5-flash-api-0514\",\"mistral-large-2407\",\"im-also-a-good-gpt2-chatbot\",\"im-a-good-gpt2-chatbot\",\"jamba-1.5-large\",\"jamba-1.5-mini\",\"gemma-2-27b-it\",\"gemma-2-9b-it\",\"gemma-2-2b-it\",\"eureka-chatbot\",\"claude-3-haiku-20240307\",\"claude-3-sonnet-20240229\",\"claude-3-opus-20240229\",\"deepseek-v2.5\",\"nemotron-4-340b\",\"llama-3-70b-instruct\",\"llama-3-8b-instruct\",\"athene-70b-0725\",\"qwen2.5-72b-instruct\",\"qwen2-72b-instruct\",\"qwen-max-0919\",\"qwen-plus-0828\",\"qwen-vl-max-0809\",\"gpt-3.5-turbo-0125\",\"yi-lightning\",\"yi-lightning-lite\",\"yi-large-preview\",\"yi-large\",\"yi-vision\",\"yi-1.5-34b-chat\",\"phi-3-mini-4k-instruct-june-2024\",\"reka-core-20240904\",\"reka-core-20240722\",\"reka-flash-20240904\",\"reka-flash-20240722\",\"command-r-plus\",\"command-r-plus-08-2024\",\"command-r\",\"command-r-08-2024\",\"codestral-2405\",\"mixtral-8x22b-instruct-v0.1\",\"mixtral-8x7b-instruct-v0.1\",\"mistral-large-2402\",\"mistral-medium\",\"pixtral-12b-2409\",\"qwen1.5-110b-chat\",\"qwen1.5-72b-chat\",\"glm-4-plus\",\"glm-4-0520\",\"dbrx-instruct\",\"internlm2_5-20b-chat\",\"internvl2-26b\"],\"all_text_models\":[\"chatgpt-4o-latest-20240903\",\"gpt-4o-mini-2024-07-18\",\"gpt-4o-2024-08-06\",\"gpt-4o-2024-05-13\",\"grok-2-2024-08-13\",\"grok-2-mini-2024-08-13\",\"test-model-1\",\"test-model-2\",\"claude-3-5-sonnet-20240620\",\"llama-3.2-vision-90b-instruct\",\"llama-3.2-vision-11b-instruct\",\"llama-3.2-3b-instruct\",\"llama-3.2-1b-instruct\",\"llama-3.1-405b-instruct-bf16\",\"llama-3.1-405b-instruct-fp8\",\"llama-3.1-70b-instruct\",\"llama-3.1-8b-instruct\",\"gemini-1.5-pro-exp-0827\",\"gemini-1.5-flash-exp-0827\",\"gemini-1.5-flash-8b-exp-0827\",\"gemini-1.5-pro-api-0514\",\"gemini-1.5-flash-api-0514\",\"mistral-large-2407\",\"gpt-4-turbo-2024-04-09\",\"gpt-4-1106-preview\",\"gpt-4-0125-preview\",\"im-also-a-good-gpt2-chatbot\",\"im-a-good-gpt2-chatbot\",\"jamba-1.5-large\",\"jamba-1.5-mini\",\"gemma-2-27b-it\",\"gemma-2-9b-it\",\"gemma-2-2b-it\",\"eureka-chatbot\",\"claude-3-haiku-20240307\",\"claude-3-sonnet-20240229\",\"claude-3-opus-20240229\",\"deepseek-v2.5\",\"nemotron-4-340b\",\"llama-3-70b-instruct\",\"llama-3-8b-instruct\",\"athene-70b-0725\",\"qwen2.5-72b-instruct\",\"qwen2-72b-instruct\",\"qwen-max-0919\",\"qwen-plus-0828\",\"qwen-vl-max-0809\",\"gpt-3.5-turbo-0125\",\"yi-lightning\",\"yi-lightning-lite\",\"yi-large-preview\",\"yi-large\",\"yi-vision\",\"yi-1.5-34b-chat\",\"phi-3-mini-4k-instruct-june-2024\",\"reka-core-20240904\",\"reka-core-20240722\",\"reka-flash-20240904\",\"reka-flash-20240722\",\"pizza-model-small\",\"pizza-model-large\",\"command-r-plus\",\"command-r-plus-08-2024\",\"command-r\",\"command-r-08-2024\",\"codestral-2405\",\"mixtral-8x22b-instruct-v0.1\",\"mixtral-8x7b-instruct-v0.1\",\"mistral-large-2402\",\"mistral-medium\",\"pixtral-12b-2409\",\"qwen1.5-110b-chat\",\"qwen1.5-72b-chat\",\"glm-4-plus\",\"glm-4-0520\",\"dbrx-instruct\",\"dbrx-next\",\"gpt-4-0613\",\"internlm2_5-20b-chat\",\"internvl2-26b\",\"dumbledore-v4\",\"gemini-1.5-flash-8b-exp-0924\",\"gemini-1.5-flash-test-5\",\"gemini-1.5-pro-002-test-sp\",\"o1-mini\",\"o1-preview\"],\"vision_models\":[\"chatgpt-4o-latest-20240903\",\"gpt-4o-mini-2024-07-18\",\"gpt-4o-2024-08-06\",\"gpt-4o-2024-05-13\",\"claude-3-5-sonnet-20240620\",\"llama-3.2-vision-90b-instruct\",\"llama-3.2-vision-11b-instruct\",\"gemini-1.5-pro-exp-0827\",\"gemini-1.5-flash-exp-0827\",\"gemini-1.5-flash-8b-exp-0827\",\"gemini-1.5-pro-api-0514\",\"gemini-1.5-flash-api-0514\",\"claude-3-haiku-20240307\",\"claude-3-sonnet-20240229\",\"claude-3-opus-20240229\",\"qwen2-vl-7b-instruct\",\"qwen-vl-max-0809\",\"yi-vision\",\"phi-3.5-vision-instruct\",\"llava-onevision-qwen2-72b-ov-chat\",\"reka-core-20240904\",\"reka-core-20240722\",\"reka-flash-20240904\",\"reka-flash-20240722\",\"pixtral-12b-2409\",\"internvl2-26b\",\"internvl2-4b\"],\"all_vision_models\":[\"chatgpt-4o-latest-20240903\",\"gpt-4o-mini-2024-07-18\",\"gpt-4o-2024-08-06\",\"gpt-4o-2024-05-13\",\"test-model-1\",\"test-model-2\",\"claude-3-5-sonnet-20240620\",\"llama-3.2-vision-90b-instruct\",\"llama-3.2-vision-11b-instruct\",\"gemini-1.5-pro-exp-0827\",\"gemini-1.5-flash-exp-0827\",\"gemini-1.5-flash-8b-exp-0827\",\"gemini-1.5-pro-api-0514\",\"gemini-1.5-flash-api-0514\",\"gpt-4-turbo-2024-04-09\",\"claude-3-haiku-20240307\",\"claude-3-sonnet-20240229\",\"claude-3-opus-20240229\",\"qwen2-vl-7b-instruct\",\"qwen-vl-max-0809\",\"yi-vision\",\"phi-3.5-vision-instruct\",\"llava-onevision-qwen2-72b-ov-chat\",\"reka-core-20240904\",\"reka-core-20240722\",\"reka-flash-20240904\",\"reka-flash-20240722\",\"pixtral-12b-2409\",\"internvl2-26b\",\"internvl2-4b\",\"dumbledore-v4\",\"gemini-1.5-flash-8b-exp-0924\",\"gemini-1.5-flash-test-5\",\"gemini-1.5-pro-002-test-sp\"],\"models\":[\"chatgpt-4o-latest-20240903\",\"gpt-4o-mini-2024-07-18\",\"gpt-4o-2024-08-06\",\"gpt-4o-2024-05-13\",\"grok-2-2024-08-13\",\"grok-2-mini-2024-08-13\",\"claude-3-5-sonnet-20240620\",\"llama-3.2-vision-90b-instruct\",\"llama-3.2-vision-11b-instruct\",\"llama-3.2-3b-instruct\",\"llama-3.2-1b-instruct\",\"llama-3.1-405b-instruct-bf16\",\"llama-3.1-405b-instruct-fp8\",\"llama-3.1-70b-instruct\",\"llama-3.1-8b-instruct\",\"gemini-1.5-pro-exp-0827\",\"gemini-1.5-flash-exp-0827\",\"gemini-1.5-flash-8b-exp-0827\",\"gemini-1.5-pro-api-0514\",\"gemini-1.5-flash-api-0514\",\"mistral-large-2407\",\"im-also-a-good-gpt2-chatbot\",\"im-a-good-gpt2-chatbot\",\"jamba-1.5-large\",\"jamba-1.5-mini\",\"gemma-2-27b-it\",\"gemma-2-9b-it\",\"gemma-2-2b-it\",\"eureka-chatbot\",\"claude-3-haiku-20240307\",\"claude-3-sonnet-20240229\",\"claude-3-opus-20240229\",\"deepseek-v2.5\",\"nemotron-4-340b\",\"llama-3-70b-instruct\",\"llama-3-8b-instruct\",\"athene-70b-0725\",\"qwen2.5-72b-instruct\",\"qwen2-72b-instruct\",\"qwen-max-0919\",\"qwen-plus-0828\",\"qwen-vl-max-0809\",\"gpt-3.5-turbo-0125\",\"yi-lightning\",\"yi-lightning-lite\",\"yi-large-preview\",\"yi-large\",\"yi-vision\",\"yi-1.5-34b-chat\",\"phi-3-mini-4k-instruct-june-2024\",\"reka-core-20240904\",\"reka-core-20240722\",\"reka-flash-20240904\",\"reka-flash-20240722\",\"command-r-plus\",\"command-r-plus-08-2024\",\"command-r\",\"command-r-08-2024\",\"codestral-2405\",\"mixtral-8x22b-instruct-v0.1\",\"mixtral-8x7b-instruct-v0.1\",\"mistral-large-2402\",\"mistral-medium\",\"pixtral-12b-2409\",\"qwen1.5-110b-chat\",\"qwen1.5-72b-chat\",\"glm-4-plus\",\"glm-4-0520\",\"dbrx-instruct\",\"internlm2_5-20b-chat\",\"internvl2-26b\",\"qwen2-vl-7b-instruct\",\"phi-3.5-vision-instruct\",\"llava-onevision-qwen2-72b-ov-chat\",\"internvl2-4b\"],\"all_models\":[\"chatgpt-4o-latest-20240903\",\"gpt-4o-mini-2024-07-18\",\"gpt-4o-2024-08-06\",\"gpt-4o-2024-05-13\",\"grok-2-2024-08-13\",\"grok-2-mini-2024-08-13\",\"test-model-1\",\"test-model-2\",\"claude-3-5-sonnet-20240620\",\"llama-3.2-vision-90b-instruct\",\"llama-3.2-vision-11b-instruct\",\"llama-3.2-3b-instruct\",\"llama-3.2-1b-instruct\",\"llama-3.1-405b-instruct-bf16\",\"llama-3.1-405b-instruct-fp8\",\"llama-3.1-70b-instruct\",\"llama-3.1-8b-instruct\",\"gemini-1.5-pro-exp-0827\",\"gemini-1.5-flash-exp-0827\",\"gemini-1.5-flash-8b-exp-0827\",\"gemini-1.5-pro-api-0514\",\"gemini-1.5-flash-api-0514\",\"mistral-large-2407\",\"gpt-4-turbo-2024-04-09\",\"gpt-4-1106-preview\",\"gpt-4-0125-preview\",\"im-also-a-good-gpt2-chatbot\",\"im-a-good-gpt2-chatbot\",\"jamba-1.5-large\",\"jamba-1.5-mini\",\"gemma-2-27b-it\",\"gemma-2-9b-it\",\"gemma-2-2b-it\",\"eureka-chatbot\",\"claude-3-haiku-20240307\",\"claude-3-sonnet-20240229\",\"claude-3-opus-20240229\",\"deepseek-v2.5\",\"nemotron-4-340b\",\"llama-3-70b-instruct\",\"llama-3-8b-instruct\",\"athene-70b-0725\",\"qwen2.5-72b-instruct\",\"qwen2-72b-instruct\",\"qwen-max-0919\",\"qwen-plus-0828\",\"qwen-vl-max-0809\",\"gpt-3.5-turbo-0125\",\"yi-lightning\",\"yi-lightning-lite\",\"yi-large-preview\",\"yi-large\",\"yi-vision\",\"yi-1.5-34b-chat\",\"phi-3-mini-4k-instruct-june-2024\",\"reka-core-20240904\",\"reka-core-20240722\",\"reka-flash-20240904\",\"reka-flash-20240722\",\"pizza-model-small\",\"pizza-model-large\",\"command-r-plus\",\"command-r-plus-08-2024\",\"command-r\",\"command-r-08-2024\",\"codestral-2405\",\"mixtral-8x22b-instruct-v0.1\",\"mixtral-8x7b-instruct-v0.1\",\"mistral-large-2402\",\"mistral-medium\",\"pixtral-12b-2409\",\"qwen1.5-110b-chat\",\"qwen1.5-72b-chat\",\"glm-4-plus\",\"glm-4-0520\",\"dbrx-instruct\",\"dbrx-next\",\"gpt-4-0613\",\"internlm2_5-20b-chat\",\"internvl2-26b\",\"dumbledore-v4\",\"gemini-1.5-flash-8b-exp-0924\",\"gemini-1.5-flash-test-5\",\"gemini-1.5-pro-002-test-sp\",\"o1-mini\",\"o1-preview\",\"qwen2-vl-7b-instruct\",\"phi-3.5-vision-instruct\",\"llava-onevision-qwen2-72b-ov-chat\",\"internvl2-4b\"]}],\"event_data\":null,\"fn_index\":13,\"trigger_id\":49,\"session_hash\":\"{{SESSION_ID}}\"}'"

# not sure what this one does
CURL_COMMAND_4 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[],\"event_data\":null,\"fn_index\":14,\"trigger_id\":49,\"session_hash\":\"{{SESSION_ID}}\"}'"


CURL_COMMAND_5 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[null,null,0.7,1,2000],\"event_data\":null,\"fn_index\":15,\"trigger_id\":49,\"session_hash\":\"{{SESSION_ID}}\"}'"


CURL_COMMAND_6 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[],\"event_data\":null,\"fn_index\":16,\"trigger_id\":49,\"session_hash\":\"{{SESSION_ID}}\"}'"

#submits preference fn_index = 1 (A is better), fn_index = 2 (B is better), fn_index = 3 (tie)
CURL_COMMAND_7 = "curl 'https://lmarena.ai/queue/join?' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'origin: https://lmarena.ai' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  --data-raw '{\"data\":[null,null,\"\",\"\"],\"event_data\":null,\"fn_index\":{{VOTE}},\"trigger_id\":45,\"session_hash\":\"{{SESSION_ID}}\"}'"


CURL_COMMAND_GET_DATA = "curl 'https://lmarena.ai/queue/data?session_hash={{SESSION_ID}}' \
  -H 'accept: text/event-stream' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'"

CURL_HEARTBEAT = "curl 'https://lmarena.ai/heartbeat/{{SESSION_ID}}' \
  -H 'accept: text/event-stream' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'cookie: {{COOKIE}}' \
  -H 'dnt: 1' \
  -H 'priority: u=1, i' \
  -H 'referer: https://lmarena.ai/' \
  -H 'sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'"