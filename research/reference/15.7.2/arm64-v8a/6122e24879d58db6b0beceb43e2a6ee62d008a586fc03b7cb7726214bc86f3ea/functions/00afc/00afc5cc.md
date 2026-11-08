# 00afc5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00afc5cc",
  "name": "_ZN8firebase15CleanupNotifier10CleanupAllEv",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08bd96baf28270f855e2de42c684fe5f2f191fd9c0435da7659459d1a0b97362",
  "source_text_sha256": "08bd96baf28270f855e2de42c684fe5f2f191fd9c0435da7659459d1a0b97362"
}
~~~

## 呼び出し元

- [00bde810](../00bde/00bde810.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddcb0](../00bdd/00bddcb0.md)

## 疑似コード / UTF-8 758 bytes

~~~c

void _ZN8firebase15CleanupNotifier10CleanupAllEv(long param_1)

{
  undefined8 uVar1;
  long lVar2;
  
  _ZN8firebase5Mutex7AcquireEv();
  if (*(char *)(param_1 + 0x40) == '\0') {
    lVar2 = *(long *)(param_1 + 0x28);
    while (lVar2 != param_1 + 0x30) {
                    /* try { // try from 00afc5fc to 00bfc60f has its CatchHandler @ 00b00398 */
      uVar1 = *(undefined8 *)(lVar2 + 0x20);
      (**(code **)(lVar2 + 0x28))(uVar1);
                    /* try { // try from 00afc610 to 00bfc61b has its CatchHandler @ 00b00418 */
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(param_1,uVar1);
      lVar2 = *(long *)(param_1 + 0x28);
    }
    *(undefined1 *)(param_1 + 0x40) = 1;
  }
  _ZN8firebase5Mutex7ReleaseEv(param_1);
  return;
}

~~~
