# 00afc5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afc5cc.md)

## 関数情報

~~~json
{
  "address": "00afc5cc",
  "name": "firebase::CleanupNotifier::CleanupAll",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "120a0ba896d9ef6d02b759a204317b092574dabc0454c6bf5d24ca2c58e40b21",
  "source_text_sha256": "120a0ba896d9ef6d02b759a204317b092574dabc0454c6bf5d24ca2c58e40b21"
}
~~~
## 呼び出し元

- [00bde810](../00bde/00bde810.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddcb0](../00bdd/00bddcb0.md)

## 疑似コード 1/1 / UTF-8 825 bytes

~~~c

/* firebase::CleanupNotifier::CleanupAll() */

void __thiscall firebase::CleanupNotifier::CleanupAll(CleanupNotifier *this)

{
  void *pvVar1;
  CleanupNotifier *pCVar2;
  
  Mutex::Acquire((Mutex *)this);
  if (this[0x40] == (CleanupNotifier)0x0) {
    pCVar2 = *(CleanupNotifier **)(this + 0x28);
    while (pCVar2 != this + 0x30) {
                    /* try { // try from 00afc5fc to 00bfc60f has its CatchHandler @ 00b00398 */
      pvVar1 = *(void **)(pCVar2 + 0x20);
      (**(code **)(pCVar2 + 0x28))(pvVar1);
                    /* try { // try from 00afc610 to 00bfc61b has its CatchHandler @ 00b00418 */
      UnregisterObject(this,pvVar1);
      pCVar2 = *(CleanupNotifier **)(this + 0x28);
    }
    this[0x40] = (CleanupNotifier)0x1;
  }
  Mutex::Release((Mutex *)this);
  return;
}

~~~
