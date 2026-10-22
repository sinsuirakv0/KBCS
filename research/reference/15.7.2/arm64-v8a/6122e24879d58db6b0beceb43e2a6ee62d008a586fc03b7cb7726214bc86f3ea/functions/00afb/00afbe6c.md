# 00afbe6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afbe6c.md)

## 関数情報

~~~json
{
  "address": "00afbe6c",
  "name": "firebase::callback::CallbackDispatcher::DispatchCallbacks",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "650a433dd204f9a54f8ff3f8af579e0a8f24a8658a8d55cae909ff5ce5427d71",
  "source_text_sha256": "650a433dd204f9a54f8ff3f8af579e0a8f24a8658a8d55cae909ff5ce5427d71"
}
~~~
## 呼び出し元

- [00bdeb70](../00bde/00bdeb70.md)

## 呼び出し先

- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bdeb40](../00bde/00bdeb40.md)

## 疑似コード 1/1 / UTF-8 3545 bytes

~~~c

/* firebase::callback::CallbackDispatcher::DispatchCallbacks() */

int __thiscall firebase::callback::CallbackDispatcher::DispatchCallbacks(CallbackDispatcher *this)

{
  Mutex *this_00;
  __shared_weak_count *p_Var1;
  CallbackEntry *this_01;
  long lVar2;
  __shared_weak_count *this_02;
  char cVar3;
  bool bVar4;
  long lVar5;
  int iVar6;
  long *plVar7;
  __shared_weak_count *p_Var8;
  
  this_00 = (Mutex *)(this + 0x18);
                    /* try { // try from 00afbe88 to 00bfbe93 has its CatchHandler @ 00b0044c */
  Mutex::Acquire(this_00);
  lVar5 = *(long *)(this + 0x10);
                    /* try { // try from 00afbe98 to 00bfbea3 has its CatchHandler @ 00b00444 */
  if (lVar5 == 0) {
    iVar6 = 0;
  }
  else {
    iVar6 = 0;
    do {
      plVar7 = *(long **)(this + 8);
      this_01 = (CallbackEntry *)plVar7[2];
      this_02 = (__shared_weak_count *)plVar7[3];
                    /* try { // try from 00afbeb4 to 00bfbec7 has its CatchHandler @ 00b00448 */
      if (this_02 != (__shared_weak_count *)0x0) {
        p_Var8 = this_02 + 8;
        do {
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(p_Var8,0x10);
          if (bVar4) {
            *(long *)p_Var8 = *(long *)p_Var8 + 1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        plVar7 = *(long **)(this + 8);
        lVar5 = *(long *)(this + 0x10);
      }
      lVar2 = *plVar7;
      *(long *)(lVar2 + 8) = plVar7[1];
      *(long *)plVar7[1] = lVar2;
      *(long *)(this + 0x10) = lVar5 + -1;
      p_Var8 = (__shared_weak_count *)plVar7[3];
      if (p_Var8 != (__shared_weak_count *)0x0) {
        p_Var1 = p_Var8 + 8;
        do {
          lVar5 = *(long *)p_Var1;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(p_Var1,0x10);
          if (bVar4) {
            *(long *)p_Var1 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
          (**(code **)(*(long *)p_Var8 + 0x10))(p_Var8);
          std::__ndk1::__shared_weak_count::__release_weak(p_Var8);
        }
      }
      operator_delete(plVar7);
      Mutex::Release(this_00);
                    /* try { // try from 00afbf34 to 00bfbf47 has its CatchHandler @ 00b0040c */
      CallbackEntry::Execute(this_01);
      iVar6 = iVar6 + 1;
      Mutex::Acquire(this_00);
      if (this_02 != (__shared_weak_count *)0x0) {
                    /* try { // try from 00afbf48 to 00bfbf4f has its CatchHandler @ 00b003f4 */
        p_Var8 = this_02 + 8;
        do {
          lVar5 = *(long *)p_Var8;
          cVar3 = '\x01';
          bVar4 = (bool)ExclusiveMonitorPass(p_Var8,0x10);
          if (bVar4) {
            *(long *)p_Var8 = lVar5 + -1;
            cVar3 = ExclusiveMonitorsStatus();
          }
        } while (cVar3 != '\0');
        if (lVar5 == 0) {
          (**(code **)(*(long *)this_02 + 0x10))(this_02);
          std::__ndk1::__shared_weak_count::__release_weak(this_02);
                    /* try { // try from 00afbf78 to 00bfbf8b has its CatchHandler @ 00b003d0 */
        }
      }
                    /* try { // try from 00afbea4 to 00bfbeb3 has its CatchHandler @ 00b00440 */
      lVar5 = *(long *)(this + 0x10);
    } while (lVar5 != 0);
  }
  Mutex::Release(this_00);
                    /* try { // try from 00afbf8c to 00bfbfa7 has its CatchHandler @ 00b003b0 */
  return iVar6;
}

~~~
