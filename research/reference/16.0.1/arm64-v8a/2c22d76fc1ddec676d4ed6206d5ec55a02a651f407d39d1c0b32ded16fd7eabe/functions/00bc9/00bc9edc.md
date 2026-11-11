# 00bc9edc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00bc9edc",
  "name": "_ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "937f498659a3cb37972eb38c3a26728ebe04ab216c180ed323f2ddd460fdaa07",
  "source_text_sha256": "937f498659a3cb37972eb38c3a26728ebe04ab216c180ed323f2ddd460fdaa07"
}
~~~

## 呼び出し元

- [00c5d920](../00c5d/00c5d920.md)

## 呼び出し先

- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5adf0](../00c5a/00c5adf0.md)
- [00c5ae00](../00c5a/00c5ae00.md)

## 疑似コード / UTF-8 1061 bytes

~~~c

void _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
                    /* catch() { ... } // from try @ 00bc9c18 with catch @ 00bc9edc */
                    /* catch() { ... } // from try @ 00bc9dc0 with catch @ 00bc9ee0 */
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
                    /* catch() { ... } // from try @ 00bc9be0 with catch @ 00bc9f20
                       catch() { ... } // from try @ 00bc9d98 with catch @ 00bc9f20 */
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
                    /* catch() { ... } // from try @ 00bc9ce8 with catch @ 00bc9f28 */
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~
