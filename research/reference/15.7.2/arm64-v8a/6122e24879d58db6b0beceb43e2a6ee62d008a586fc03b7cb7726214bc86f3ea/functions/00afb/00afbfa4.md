# 00afbfa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afc0b0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afbfa4",
  "name": "_ZN8firebase8callback18CallbackDispatcherD2Ev",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6900d42fd4446b3377be9c13c416cf9386ecf8dc2e25e41b13e3e8165a932f0",
  "source_text_sha256": "f6900d42fd4446b3377be9c13c416cf9386ecf8dc2e25e41b13e3e8165a932f0"
}
~~~

## 呼び出し元

- [00bdeb80](../00bde/00bdeb80.md)

## 呼び出し先

- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddb50](../00bdd/00bddb50.md)
- [00bdde60](../00bdd/00bdde60.md)

## 関連文字列（未確認候補）

~~~text
"Callback dispatcher shut down with %d pending callbacks"
~~~

## 疑似コード / UTF-8 3223 bytes

~~~c

void _ZN8firebase8callback18CallbackDispatcherD2Ev(long *param_1)

{
  long *plVar1;
  long *plVar2;
  char cVar3;
  bool bVar4;
  long lVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
  plVar2 = param_1 + 3;
  _ZN8firebase5Mutex7AcquireEv(plVar2);
  if (param_1[2] != 0) {
    _ZN8firebase10LogWarningEPKcz("Callback dispatcher shut down with %d pending callbacks");
    lVar5 = param_1[2];
    while (lVar5 != 0) {
      lVar5 = *param_1;
      plVar7 = *(long **)(lVar5 + 0x18);
      *(undefined8 *)(lVar5 + 0x10) = 0;
      *(undefined8 *)(lVar5 + 0x18) = 0;
      if (plVar7 != (long *)0x0) {
        plVar8 = plVar7 + 1;
        do {
          lVar5 = *plVar8;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(plVar8,0x10);
          if (bVar4) {
            *plVar8 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
          (**(code **)(*plVar7 + 0x10))(plVar7);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        }
      }
      plVar7 = (long *)*param_1;
      lVar5 = *plVar7;
      *(long *)(lVar5 + 8) = plVar7[1];
      *(long *)plVar7[1] = lVar5;
      param_1[2] = param_1[2] + -1;
      plVar8 = (long *)plVar7[3];
      if (plVar8 != (long *)0x0) {
        plVar1 = plVar8 + 1;
        do {
          lVar5 = *plVar1;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(plVar1,0x10);
          if (bVar4) {
            *plVar1 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
          (**(code **)(*plVar8 + 0x10))(plVar8);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
        }
      }
                    /* try { // try from 00afbfe8 to 00bfbfef has its CatchHandler @ 00b00380 */
      _ZdlPv(plVar7);
      lVar5 = param_1[2];
                    /* try { // try from 00afbff0 to 00bfc0eb has its CatchHandler @ 00af560c */
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(plVar2);
  _ZN8firebase5MutexD1Ev(param_1 + 8);
  _ZN8firebase5MutexD1Ev(plVar2);
  if (param_1[2] != 0) {
    lVar5 = *param_1;
    plVar2 = (long *)param_1[1];
    lVar6 = *plVar2;
    *(undefined8 *)(lVar6 + 8) = *(undefined8 *)(lVar5 + 8);
    **(long **)(lVar5 + 8) = lVar6;
    param_1[2] = 0;
    while (plVar2 != param_1) {
                    /* try { // try from 00afc0ec to 00bfc10f has its CatchHandler @ 00b00450 */
      plVar7 = (long *)plVar2[3];
      plVar8 = (long *)plVar2[1];
      if (plVar7 != (long *)0x0) {
        plVar1 = plVar7 + 1;
        do {
          lVar5 = *plVar1;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(plVar1,0x10);
          if (bVar4) {
            *plVar1 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
                    /* try { // try from 00afc110 to 00bfc11b has its CatchHandler @ 00b003a4 */
          (**(code **)(*plVar7 + 0x10))(plVar7);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        }
      }
      _ZdlPv(plVar2);
      plVar2 = plVar8;
    }
  }
  return;
}

~~~
