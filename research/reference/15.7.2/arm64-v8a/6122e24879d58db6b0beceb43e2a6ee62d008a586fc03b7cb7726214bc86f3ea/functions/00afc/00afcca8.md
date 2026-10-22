# 00afcca8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afcca8.md)

## 関数情報

~~~json
{
  "address": "00afcca8",
  "name": "firebase::CleanupNotifier::FindByOwner",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "beb4f684ddc0f581455e0af4a4d41a8fc32790d2d16506e2be485f27645e4c38",
  "source_text_sha256": "beb4f684ddc0f581455e0af4a4d41a8fc32790d2d16506e2be485f27645e4c38"
}
~~~
## 呼び出し元

- [00bddc90](../00bdd/00bddc90.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード 1/1 / UTF-8 1246 bytes

~~~c

/* firebase::CleanupNotifier::FindByOwner(void*) */

long firebase::CleanupNotifier::FindByOwner(void *param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  Mutex *this;
  long lVar4;
  
                    /* try { // try from 00afccac to 00bfccb3 has its CatchHandler @ 00aff3cc */
  this = *(Mutex **)PTR_cleanup_notifiers_by_owner_mutex__00c1b898;
  Mutex::Acquire(this);
  if (*(long *)PTR_cleanup_notifiers_by_owner__00c1b890 != 0) {
                    /* try { // try from 00afccdc to 00bfccf3 has its CatchHandler @ 00aff3c8 */
    plVar1 = (long *)(*(long *)PTR_cleanup_notifiers_by_owner__00c1b890 + 8);
    plVar3 = (long *)*plVar1;
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
                    /* try { // try from 00afccf4 to 00bfcd67 has its CatchHandler @ 00af560c */
        if ((void *)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
        plVar3 = (long *)plVar3[(void *)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
      if ((plVar2 != plVar1) && ((void *)plVar2[4] <= param_1)) {
        lVar4 = plVar2[5];
        goto LAB_00afcd18;
      }
    }
  }
  lVar4 = 0;
LAB_00afcd18:
  Mutex::Release(this);
  return lVar4;
}

~~~
