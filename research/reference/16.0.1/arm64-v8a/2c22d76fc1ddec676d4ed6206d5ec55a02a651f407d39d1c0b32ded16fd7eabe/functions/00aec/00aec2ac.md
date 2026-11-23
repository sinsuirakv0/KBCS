# 00aec2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aebe84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0064.md#compare-100dc33342f0c1a471f0bf4dbf8b17a5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0069.md#compare-7bfa297c4e0a30c3d8bee0a90a83af2c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aec2ac",
  "name": "FUN_00aec2ac",
  "size": 640,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d133c3f4303d666934a7809cb984a93ab963c76c3d14fde8fd3b874cb8029a1",
  "source_text_sha256": "4d133c3f4303d666934a7809cb984a93ab963c76c3d14fde8fd3b874cb8029a1"
}
~~~

## 呼び出し元

- [00aec52c](../00aec/00aec52c.md)

## 呼び出し先

- [0067e5e8](../0067e/0067e5e8.md)
- [00682324](../00682/00682324.md)
- [006b21e4](../006b2/006b21e4.md)
- [006b7694](../006b7/006b7694.md)
- [00c53d00](../00c53/00c53d00.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 4233 bytes

~~~c

void FUN_00aec2ac(undefined8 *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  void *pvVar3;
  long *plVar4;
  
  *param_1 = &PTR_FUN_00c8d940;
                    /* try { // try from 00aec2d0 to 00bec2e3 has its CatchHandler @ 00aec834 */
  FUN_0067e5e8(param_1 + 0xa2);
  FUN_006b7694(param_1 + 0x9f,param_1[0xa0]);
  plVar4 = (long *)param_1[0x9e];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
                    /* try { // try from 00aec2fc to 00bec307 has its CatchHandler @ 00aec828 */
    (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* try { // try from 00aec308 to 00bec313 has its CatchHandler @ 00aec810 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x9c];
                    /* try { // try from 00aec314 to 00bec31f has its CatchHandler @ 00aec800 */
                    /* try { // try from 00aec320 to 00bec35f has its CatchHandler @ 00aec250 */
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x9a];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
                    /* try { // try from 00aec360 to 00bec367 has its CatchHandler @ 00aec7fc */
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x98];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
                    /* try { // try from 00aec398 to 00bec3a3 has its CatchHandler @ 00aec7e0 */
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x96];
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  FUN_006b21e4(param_1 + 0x7e);
  FUN_006b21e4(param_1 + 0x68);
  puVar1 = (void *)param_1[0x65];
  while (puVar1 != (void *)0x0) {
    plVar4 = (long *)puVar1[4];
    pvVar3 = (void *)*puVar1;
    if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    _ZdlPv(puVar1);
    puVar1 = pvVar3;
  }
  pvVar3 = (void *)param_1[99];
  param_1[99] = 0;
  if (pvVar3 != (void *)0x0) {
    _ZdlPv(pvVar3);
  }
  puVar1 = (void *)param_1[0x60];
  while (puVar1 != (void *)0x0) {
    plVar4 = (long *)puVar1[4];
    pvVar3 = (void *)*puVar1;
                    /* try { // try from 00aec4fc to 00bec50f has its CatchHandler @ 00aec854 */
    if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0)
       ) {
      (**(code **)(*plVar4 + 0x10))(plVar4);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
    }
    _ZdlPv(puVar1);
    puVar1 = pvVar3;
  }
  pvVar3 = (void *)param_1[0x5e];
  param_1[0x5e] = 0;
  if (pvVar3 != (void *)0x0) {
                    /* try { // try from 00aec40c to 00bec41b has its CatchHandler @ 00aec868 */
    _ZdlPv(pvVar3);
  }
  plVar4 = (long *)param_1[0x5d];
  *param_1 = &PTR_FUN_00c78330;
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  plVar4 = (long *)param_1[0x5b];
                    /* try { // try from 00aec450 to 00bec463 has its CatchHandler @ 00aec858 */
  *param_1 = &PTR_FUN_00c74810;
                    /* try { // try from 00aec464 to 00bec4fb has its CatchHandler @ 00aec250 */
  if ((plVar4 != (long *)0x0) && (lVar2 = FUN_00c53d00(0xffffffffffffffff,plVar4 + 1), lVar2 == 0))
  {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  FUN_00682324(param_1);
  return;
}

~~~
