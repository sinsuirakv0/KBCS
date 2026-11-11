# 00afadac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afadac",
  "name": "FUN_00afadac",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "880f3729ec794c696796f3581cf89594202a8f94ae95ae50a6940ab8af384780",
  "source_text_sha256": "880f3729ec794c696796f3581cf89594202a8f94ae95ae50a6940ab8af384780"
}
~~~

## 呼び出し元

- [005fe66c](../005fe/005fe66c.md)
- [00700af8](../00700/00700af8.md)
- [00707ee0](../00707/00707ee0.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 280 bytes

~~~c

bool FUN_00afadac(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afadc0 to 00bfae0b has its CatchHandler @ 00afb3ec */
  lVar1 = FUN_008514f8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a84) != 0;
}

~~~
