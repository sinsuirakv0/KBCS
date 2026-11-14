# 00bc5bbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bc5bbc",
  "name": "_ZNK8firebase13remote_config8internal20RemoteConfigInternal11InitializedEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "764e26167b4431b9a1e02d10842c7068e6e4b96622bb95044d19dc2f656452c3",
  "source_text_sha256": "764e26167b4431b9a1e02d10842c7068e6e4b96622bb95044d19dc2f656452c3"
}
~~~

## 呼び出し元

- [00c5e930](../00c5e/00c5e930.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 143 bytes

~~~c

bool _ZNK8firebase13remote_config8internal20RemoteConfigInternal11InitializedEv(long param_1)

{
  return *(long *)(param_1 + 0x198) != 0;
}

~~~
