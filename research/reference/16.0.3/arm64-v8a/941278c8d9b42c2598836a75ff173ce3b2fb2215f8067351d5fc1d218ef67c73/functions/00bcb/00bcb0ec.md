# 00bcb0ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcb0ec",
  "name": "_INIT_289",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "604bce8a8d4c315b521f55afa122b1fc03cf2af27a223f9b0bc643b9190b35f8",
  "source_text_sha256": "604bce8a8d4c315b521f55afa122b1fc03cf2af27a223f9b0bc643b9190b35f8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58ed0](../00c58/00c58ed0.md)
- [00c5bd20](../00c5b/00c5bd20.md)

## 疑似コード / UTF-8 649 bytes

~~~c

void _INIT_289(void)

{
  undefined *puVar1;
  undefined *puVar2;
  
  puVar1 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18;
  puVar2 = PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 +
           4;
  *(undefined4 *)
   PTR__ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E_00c9ca18 = 0;
  _ZN8firebase5MutexC1ENS0_4ModeE(puVar2,1);
                    /* try { // try from 00bcb124 to 00ccb127 has its CatchHandler @ 00bcb2ac */
  __cxa_atexit(PTR__ZN8firebase8internal14ReferenceCountD2Ev_00c9ca38,puVar1,&PTR_LOOP_00c64030);
  return;
}

~~~
