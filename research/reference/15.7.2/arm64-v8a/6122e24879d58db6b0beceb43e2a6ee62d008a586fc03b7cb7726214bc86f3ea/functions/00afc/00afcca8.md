# 00afcca8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afcdb4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afcca8",
  "name": "_ZN8firebase15CleanupNotifier11FindByOwnerEPv",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "945884a133c7c30a4f3a8d6f550d306e6c1e274b7de88ea4dc3a39679bbde19d",
  "source_text_sha256": "945884a133c7c30a4f3a8d6f550d306e6c1e274b7de88ea4dc3a39679bbde19d"
}
~~~

## 呼び出し元

- [00bddc90](../00bdd/00bddc90.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)

## 疑似コード / UTF-8 1334 bytes

~~~c

long _ZN8firebase15CleanupNotifier11FindByOwnerEPv(ulong param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  
                    /* try { // try from 00afccac to 00bfccb3 has its CatchHandler @ 00aff3cc */
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b898;
  _ZN8firebase5Mutex7AcquireEv(uVar4);
  if (*(long *)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b890 != 0) {
                    /* try { // try from 00afccdc to 00bfccf3 has its CatchHandler @ 00aff3c8 */
    plVar1 = (long *)(*(long *)
                       PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b890 + 8)
    ;
    plVar3 = (long *)*plVar1;
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
                    /* try { // try from 00afccf4 to 00bfcd67 has its CatchHandler @ 00af560c */
        if ((ulong)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
        plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
      if ((plVar2 != plVar1) && ((ulong)plVar2[4] <= param_1)) {
        lVar5 = plVar2[5];
        goto LAB_00afcd18;
      }
    }
  }
  lVar5 = 0;
LAB_00afcd18:
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
  return lVar5;
}

~~~
