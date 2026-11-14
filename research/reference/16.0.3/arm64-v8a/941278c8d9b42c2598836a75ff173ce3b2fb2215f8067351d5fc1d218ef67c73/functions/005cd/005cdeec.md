# 005cdeec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "005cdeec",
  "name": "FUN_005cdeec",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c5ebf4077e632ad724185c7f648b3fa8f78c7d7520b2f93c30417cd1e6238341",
  "source_text_sha256": "c5ebf4077e632ad724185c7f648b3fa8f78c7d7520b2f93c30417cd1e6238341"
}
~~~

## 呼び出し元

- [005cda50](../005cd/005cda50.md)

## 呼び出し先

- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c5b850](../00c5b/00c5b850.md)

## 疑似コード / UTF-8 551 bytes

~~~c

void FUN_005cdeec(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
                    /* try { // try from 005cdf08 to 006cdf0f has its CatchHandler @ 005cdf3c */
  _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE(uVar1,0x11);
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 005cdf20 to 006cdf37 has its CatchHandler @ 005cdf38 */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c9c450,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c9c458);
}

~~~
