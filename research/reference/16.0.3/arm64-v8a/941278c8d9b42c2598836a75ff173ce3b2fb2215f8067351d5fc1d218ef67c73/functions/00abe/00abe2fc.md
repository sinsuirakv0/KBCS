# 00abe2fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00abe2fc",
  "name": "FUN_00abe2fc",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42294078cecab3d9c50160d6103feae2d77981b23c3bc858887ab937e16ef6b8",
  "source_text_sha256": "42294078cecab3d9c50160d6103feae2d77981b23c3bc858887ab937e16ef6b8"
}
~~~

## 呼び出し元

- [0072f498](../0072f/0072f498.md)
- [0072f548](../0072f/0072f548.md)
- [0073077c](../00730/0073077c.md)
- [00731814](../00731/00731814.md)
- [00731930](../00731/00731930.md)

## 呼び出し先

- [00c594f0](../00c59/00c594f0.md)

## 疑似コード / UTF-8 382 bytes

~~~c

bool FUN_00abe2fc(long param_1,wchar_t param_2)

{
  wchar_t *pwVar1;
  wchar_t *pwVar2;
  
  pwVar2 = *(wchar_t **)(param_1 + 0x38);
  pwVar1 = wmemchr(*(wchar_t **)(param_1 + 0x30),param_2,
                   (long)pwVar2 - (long)*(wchar_t **)(param_1 + 0x30) >> 2);
  if (pwVar1 != (wchar_t *)0x0) {
    pwVar2 = pwVar1;
  }
  return pwVar2 != *(wchar_t **)(param_1 + 0x38);
}

~~~
