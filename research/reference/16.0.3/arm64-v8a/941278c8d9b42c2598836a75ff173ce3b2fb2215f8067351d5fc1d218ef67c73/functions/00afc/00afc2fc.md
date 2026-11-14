# 00afc2fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00afc2fc",
  "name": "FUN_00afc2fc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b397a79ded0b99a318b98393b480746e1d973d6e633d203610fdd2f967c77b68",
  "source_text_sha256": "b397a79ded0b99a318b98393b480746e1d973d6e633d203610fdd2f967c77b68"
}
~~~

## 呼び出し元

- [00a50418](../00a50/00a50418.md)
- [00a53028](../00a53/00a53028.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

## 疑似コード / UTF-8 478 bytes

~~~c

void FUN_00afc2fc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* catch() { ... } // from try @ 00afc15c with catch @ 00afc300 */
  lVar1 = FUN_008524fc();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b68) = param_3;
                    /* catch() { ... } // from try @ 00afc064 with catch @ 00afc340 */
                    /* catch() { ... } // from try @ 00afbfec with catch @ 00afc344 */
  return;
}

~~~
