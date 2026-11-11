# 00b5bcac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b5bcac",
  "name": "_ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df9c576ac2d452adfeaff7332fb85e3283aff6828ce890042412a1dd84b9d4eb",
  "source_text_sha256": "df9c576ac2d452adfeaff7332fb85e3283aff6828ce890042412a1dd84b9d4eb"
}
~~~

## 呼び出し元

- [00c5bb10](../00c5b/00c5bb10.md)

## 呼び出し先

- [00b5c4f4](../00b5c/00b5c4f4.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)

## 疑似コード / UTF-8 1529 bytes

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
  
  plVar4 = (long *)_Znwm(0x30);
  plVar4[2] = 0;
  puVar3 = 
  PTR__ZTVNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEEE_00c9b788
  ;
  plVar8 = plVar4 + 1;
  *plVar8 = 0;
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
  if (lVar6 == 0) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  return plVar7;
}

~~~
