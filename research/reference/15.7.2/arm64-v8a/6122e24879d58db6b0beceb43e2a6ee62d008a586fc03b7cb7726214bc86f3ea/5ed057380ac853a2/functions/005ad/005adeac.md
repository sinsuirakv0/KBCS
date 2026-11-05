# 005adeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "756a7827e220773d521f4fd07b40145174d7553963331fcdb7ee4ba897c3c51c",
  "source_text_sha256": "756a7827e220773d521f4fd07b40145174d7553963331fcdb7ee4ba897c3c51c"
}
~~~
## 呼び出し元

- [005ab944](../005ab/005ab944.md)
- [005adef8](../005ad/005adef8.md)
- [005ae3c8](../005ae/005ae3c8.md)
- [005ae654](../005ae/005ae654.md)

## 呼び出し先

- [00bdafa0](../00bda/00bdafa0.md)
- [00bdafc0](../00bda/00bdafc0.md)
- [00bdd860](../00bdd/00bdd860.md)

## 疑似コード 1/1 / UTF-8 354 bytes

~~~c

void FUN_005adeac(void)

{
  undefined8 uVar1;
  
  uVar1 = __cxa_allocate_exception(0x18);
  _ZNSt6__ndk111regex_errorC2ENS_15regex_constants10error_typeE(uVar1,5);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(uVar1,PTR__ZTINSt6__ndk111regex_errorE_00c1b4b8,
              PTR__ZNSt6__ndk111regex_errorD1Ev_00c1b4c0);
}

~~~
