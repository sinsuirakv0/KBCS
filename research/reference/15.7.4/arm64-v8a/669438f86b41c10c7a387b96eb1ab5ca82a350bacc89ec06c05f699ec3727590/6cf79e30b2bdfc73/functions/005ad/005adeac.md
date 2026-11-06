# 005adeac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](005adeac.md)

## 関数情報

~~~json
{
  "address": "005adeac",
  "name": "FUN_005adeac",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4fb5f1eacf03de2a40b80658e2c4635b43896c66cf649d44ba65506bb0937d2d",
  "source_text_sha256": "4fb5f1eacf03de2a40b80658e2c4635b43896c66cf649d44ba65506bb0937d2d"
}
~~~
## 呼び出し元

- [005ab944](../005ab/005ab944.md)
- [005adef8](../005ad/005adef8.md)
- [005ae3c8](../005ae/005ae3c8.md)
- [005ae654](../005ae/005ae654.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb0c0](../00bdb/00bdb0c0.md)
- [00bdd960](../00bdd/00bdd960.md)

## 疑似コード 1/1 / UTF-8 354 bytes

~~~c

void FUN_005adeac(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE(uVar1,5);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c1b5b8,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c1b5c0);
}

~~~
