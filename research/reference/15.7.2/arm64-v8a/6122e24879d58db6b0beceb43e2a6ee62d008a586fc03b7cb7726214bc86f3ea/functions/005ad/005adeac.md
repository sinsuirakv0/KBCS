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
  "source_sha256": "3744ffca2852f6fde98e3e548a3e892b0807f4d7fe665bd51fde8e2916f44358",
  "source_text_sha256": "3744ffca2852f6fde98e3e548a3e892b0807f4d7fe665bd51fde8e2916f44358"
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

## 疑似コード 1/1 / UTF-8 311 bytes

~~~c

void FUN_005adeac(void)

{
  regex_error *prVar1;
  
  prVar1 = (regex_error *)__cxa_allocate_exception(0x18);
  std::__ndk1::regex_error::regex_error(prVar1,5);
                    /* WARNING: Subroutine does not return */
  __cxa_throw(prVar1,PTR_typeinfo_00c1b4b8,PTR__regex_error_00c1b4c0);
}

~~~
