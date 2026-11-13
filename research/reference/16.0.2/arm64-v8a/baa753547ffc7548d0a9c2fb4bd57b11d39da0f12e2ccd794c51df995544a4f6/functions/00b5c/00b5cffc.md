# 00b5cffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00b5cffc",
  "name": "_ZN8firebase15CleanupNotifier11FindByOwnerEPv",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93e51db9ef4e727ba91f63c583ba5d3ba0b762329134cf978422309ffb4d54c9",
  "source_text_sha256": "93e51db9ef4e727ba91f63c583ba5d3ba0b762329134cf978422309ffb4d54c9"
}
~~~

## 呼び出し元

- [00c5acc0](../00c5a/00c5acc0.md)

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)

## 疑似コード / UTF-8 3044 bytes

~~~c

long _ZN8firebase15CleanupNotifier11FindByOwnerEPv(ulong param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  
                    /* catch() { ... } // from try @ 00b564c8 with catch @ 00b5cffc */
                    /* catch() { ... } // from try @ 00b56468 with catch @ 00b5d000 */
                    /* catch() { ... } // from try @ 00b5645c with catch @ 00b5d004 */
                    /* catch() { ... } // from try @ 00b563ac with catch @ 00b5d008 */
                    /* catch() { ... } // from try @ 00b56304 with catch @ 00b5d00c */
                    /* catch() { ... } // from try @ 00b562f8 with catch @ 00b5d010 */
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c9b868;
                    /* catch() { ... } // from try @ 00b562e0 with catch @ 00b5d018 */
  _ZN8firebase5Mutex7AcquireEv(uVar4);
                    /* catch() { ... } // from try @ 00b5628c with catch @ 00b5d020 */
                    /* catch() { ... } // from try @ 00b56280 with catch @ 00b5d024 */
                    /* catch() { ... } // from try @ 00b56268 with catch @ 00b5d02c */
  if (*(long *)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c9b860 != 0) {
    plVar1 = (long *)(*(long *)
                       PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c9b860 + 8)
    ;
    plVar3 = (long *)*plVar1;
                    /* catch() { ... } // from try @ 00b561f4 with catch @ 00b5d034 */
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
                    /* catch() { ... } // from try @ 00b561cc with catch @ 00b5d040 */
                    /* catch() { ... } // from try @ 00b56178 with catch @ 00b5d048 */
        if ((ulong)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
                    /* catch() { ... } // from try @ 00b5616c with catch @ 00b5d04c */
        plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00b56150 with catch @ 00b5d054 */
                    /* catch() { ... } // from try @ 00b560e8 with catch @ 00b5d05c */
                    /* catch() { ... } // from try @ 00b560dc with catch @ 00b5d060 */
      if ((plVar2 != plVar1) && ((ulong)plVar2[4] <= param_1)) {
                    /* catch() { ... } // from try @ 00b55fdc with catch @ 00b5d084 */
        lVar5 = plVar2[5];
                    /* catch() { ... } // from try @ 00b55fd0 with catch @ 00b5d088 */
        goto LAB_00b5d06c;
      }
    }
  }
                    /* catch() { ... } // from try @ 00b560c0 with catch @ 00b5d068 */
  lVar5 = 0;
LAB_00b5d06c:
                    /* catch() { ... } // from try @ 00b5606c with catch @ 00b5d070 */
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
                    /* catch() { ... } // from try @ 00b56060 with catch @ 00b5d074 */
                    /* catch() { ... } // from try @ 00b56044 with catch @ 00b5d07c */
  return lVar5;
}

~~~
