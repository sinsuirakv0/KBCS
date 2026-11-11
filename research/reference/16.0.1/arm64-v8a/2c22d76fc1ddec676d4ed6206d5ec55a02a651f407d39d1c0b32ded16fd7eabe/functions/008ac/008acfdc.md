# 008acfdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "008acfdc",
  "name": "FUN_008acfdc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "633fbb7c19a3cdee9af151a82bfa9d5b3b15d24994ef657ec322e07e0f748516",
  "source_text_sha256": "633fbb7c19a3cdee9af151a82bfa9d5b3b15d24994ef657ec322e07e0f748516"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b9178](../008b9/008b9178.md)

## 疑似コード / UTF-8 745 bytes

~~~c

void FUN_008acfdc(undefined8 param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
                    /* catch() { ... } // from try @ 008ace20 with catch @ 008acfe8 */
  if ((*param_3 == 2) && (*param_4 == 0)) {
                    /* catch() { ... } // from try @ 008acdf0 with catch @ 008acff8 */
    uVar2 = *param_2;
    uVar1 = FUN_0047acf4();
                    /* catch() { ... } // from try @ 008acdcc with catch @ 008ad00c */
    FUN_0047cdd4(uVar1,0xb,0);
                    /* catch() { ... } // from try @ 008acd60 with catch @ 008ad01c */
    FUN_008b9178(uVar2);
    return;
  }
                    /* catch() { ... } // from try @ 008acd50 with catch @ 008ad020 */
  return;
}

~~~
