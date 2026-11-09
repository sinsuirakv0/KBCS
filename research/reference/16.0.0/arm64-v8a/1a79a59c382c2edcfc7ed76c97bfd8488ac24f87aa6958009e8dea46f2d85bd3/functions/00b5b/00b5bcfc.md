# 00b5bcfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b5bcfc",
  "name": "_ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "616db4f575b13c5b7d6812933dcc2e0b3234d6cb09ddd7e5b3abac0b880933be",
  "source_text_sha256": "616db4f575b13c5b7d6812933dcc2e0b3234d6cb09ddd7e5b3abac0b880933be"
}
~~~

## 呼び出し元

- [00c5b730](../00c5b/00c5b730.md)

## 呼び出し先

- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5b700](../00c5b/00c5b700.md)

## 疑似コード / UTF-8 2456 bytes

~~~c

int _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv(long param_1)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  long lVar4;
  long *plVar5;
  char cVar6;
  bool bVar7;
  long lVar8;
  int iVar9;
  long *plVar10;
  long *plVar11;
  
  lVar1 = param_1 + 0x18;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar8 = *(long *)(param_1 + 0x10);
  if (lVar8 == 0) {
    iVar9 = 0;
  }
  else {
    iVar9 = 0;
    do {
      plVar10 = *(long **)(param_1 + 8);
      lVar3 = plVar10[2];
      plVar5 = (long *)plVar10[3];
      if (plVar5 != (long *)0x0) {
        plVar10 = plVar5 + 1;
        do {
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = *plVar10 + 1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        plVar10 = *(long **)(param_1 + 8);
        lVar8 = *(long *)(param_1 + 0x10);
      }
      lVar4 = *plVar10;
      *(long *)(lVar4 + 8) = plVar10[1];
      *(long *)plVar10[1] = lVar4;
      *(long *)(param_1 + 0x10) = lVar8 + -1;
      plVar11 = (long *)plVar10[3];
      if (plVar11 != (long *)0x0) {
        plVar2 = plVar11 + 1;
        do {
          lVar8 = *plVar2;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar2,0x10);
          if (bVar7) {
            *plVar2 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar11 + 0x10))(plVar11);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
        }
      }
      _ZdlPv(plVar10);
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      _ZN8firebase8callback13CallbackEntry7ExecuteEv(lVar3);
      iVar9 = iVar9 + 1;
      _ZN8firebase5Mutex7AcquireEv(lVar1);
      if (plVar5 != (long *)0x0) {
        plVar10 = plVar5 + 1;
        do {
          lVar8 = *plVar10;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar5 + 0x10))(plVar5);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
        }
      }
      lVar8 = *(long *)(param_1 + 0x10);
    } while (lVar8 != 0);
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  return iVar9;
}

~~~
