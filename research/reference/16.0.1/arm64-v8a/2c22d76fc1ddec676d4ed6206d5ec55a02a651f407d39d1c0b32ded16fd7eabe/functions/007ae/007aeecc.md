# 007aeecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "007aeecc",
  "name": "FUN_007aeecc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eba589f2cdcd30c10f97306385f911ab1347f9bc439f0abfcab593a1a28fab0f",
  "source_text_sha256": "eba589f2cdcd30c10f97306385f911ab1347f9bc439f0abfcab593a1a28fab0f"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb20](../0043b/0043bb20.md)

## 疑似コード / UTF-8 568 bytes

~~~c

void FUN_007aeecc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  *param_2 = &PTR_FUN_00c7a718;
  if ((*(byte *)(param_1 + 8) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = *(undefined8 *)(param_1 + 8);
    param_2[3] = *(undefined8 *)(param_1 + 0x18);
                    /* catch() { ... } // from try @ 007ae04c with catch @ 007aeef0 */
    param_2[2] = uVar2;
    param_2[1] = uVar1;
    return;
  }
  FUN_0043bb20(param_2 + 1,*(undefined8 *)(param_1 + 0x18),*(undefined8 *)(param_1 + 0x10));
  return;
}

~~~
