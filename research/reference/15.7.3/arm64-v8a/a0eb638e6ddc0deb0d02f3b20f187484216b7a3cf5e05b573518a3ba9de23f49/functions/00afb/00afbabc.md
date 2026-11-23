# 00afbabc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afb9f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb9f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0062.md#compare-f522d4619b420b1b60ad858483f8dea8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbabc",
  "name": "_ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3ab303b97dddb6a6409ba8b6c8323975b9113eb1eb1a54ac2b6c6bff82a6ce8",
  "source_text_sha256": "d3ab303b97dddb6a6409ba8b6c8323975b9113eb1eb1a54ac2b6c6bff82a6ce8"
}
~~~

## 呼び出し元

- [00bdec00](../00bde/00bdec00.md)

## 呼び出し先

- [00afc304](../00afc/00afc304.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

## 疑似コード / UTF-8 2111 bytes

~~~c

long * _ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE
                 (long *param_1,long param_2)

{
  char cVar1;
  bool bVar2;
  undefined *puVar3;
  long *plVar4;
  long *plVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
                    /* try { // try from 00afbad4 to 00bfbaef has its CatchHandler @ 00aff42c */
  plVar4 = (long *)_Znwm(0x30);
  plVar4[2] = 0;
  puVar3 = 
  PTR__ZTVNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEEE_00c1b938
  ;
  plVar8 = plVar4 + 1;
  *plVar8 = 0;
                    /* try { // try from 00afbb00 to 00bfbb07 has its CatchHandler @ 00aff428 */
  *plVar4 = (long)(puVar3 + 0x10);
  plVar7 = plVar4 + 3;
  *plVar7 = param_2;
  plVar4[4] = (long)(param_1 + 8);
  *(undefined1 *)(plVar4 + 5) = 0;
  _ZN8firebase5Mutex7AcquireEv(param_1 + 3);
  plVar5 = (long *)_Znwm(0x20);
  plVar5[2] = (long)plVar7;
  plVar5[3] = (long)plVar4;
  do {
                    /* try { // try from 00afbb30 to 00bfbb47 has its CatchHandler @ 00aff424 */
    cVar1 = '\x01';
    bVar2 = (bool)ExclusiveMonitorPass(plVar8,0x10);
    if (bVar2) {
      *plVar8 = *plVar8 + 1;
      cVar1 = ExclusiveMonitorsStatus();
    }
  } while (cVar1 != '\0');
  lVar6 = *param_1;
  *plVar5 = lVar6;
  plVar5[1] = (long)param_1;
  *(long **)(lVar6 + 8) = plVar5;
  *param_1 = (long)plVar5;
                    /* try { // try from 00afbb58 to 00bfbb6f has its CatchHandler @ 00b0037c */
  param_1[2] = param_1[2] + 1;
  _ZN8firebase5Mutex7ReleaseEv(param_1 + 3);
  do {
    lVar6 = *plVar8;
    cVar1 = '\x01';
    bVar2 = (bool)ExclusiveMonitorPass(plVar8,0x10);
    if (bVar2) {
      *plVar8 = lVar6 + -1;
      cVar1 = ExclusiveMonitorsStatus();
    }
  } while (cVar1 != '\0');
                    /* try { // try from 00afbb70 to 00bfbb77 has its CatchHandler @ 00aff420 */
  if (lVar6 == 0) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
                    /* try { // try from 00afbba0 to 00bfbbbb has its CatchHandler @ 00aff41c */
  return plVar7;
}

~~~
