# 00afbfa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afbfa4.md)

## 関数情報

~~~json
{
  "address": "00afbfa4",
  "name": "firebase::callback::CallbackDispatcher::~CallbackDispatcher",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23f910a9abfe3970c95bdb86777637eec0aa1186130a26f71b9e8b296a911dd9",
  "source_text_sha256": "23f910a9abfe3970c95bdb86777637eec0aa1186130a26f71b9e8b296a911dd9"
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
## 疑似コード 1/1 / UTF-8 3808 bytes

~~~c

/* firebase::callback::CallbackDispatcher::~CallbackDispatcher() */

void __thiscall
firebase::callback::CallbackDispatcher::~CallbackDispatcher(CallbackDispatcher *this)

{
  Mutex *this_00;
  __shared_weak_count *p_Var1;
  CallbackDispatcher *pCVar2;
  char cVar3;
  bool bVar4;
  long lVar5;
  long lVar6;
  long *plVar7;
  __shared_weak_count *p_Var8;
  CallbackDispatcher *pCVar9;
  
  this_00 = (Mutex *)(this + 0x18);
  Mutex::Acquire(this_00);
  if (*(long *)(this + 0x10) != 0) {
    LogWarning("Callback dispatcher shut down with %d pending callbacks");
    lVar5 = *(long *)(this + 0x10);
    while (lVar5 != 0) {
      lVar5 = *(long *)this;
      p_Var8 = *(__shared_weak_count **)(lVar5 + 0x18);
      *(undefined8 *)(lVar5 + 0x10) = 0;
      *(undefined8 *)(lVar5 + 0x18) = 0;
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
      plVar7 = *(long **)this;
      lVar5 = *plVar7;
      *(long *)(lVar5 + 8) = plVar7[1];
      *(long *)plVar7[1] = lVar5;
      *(long *)(this + 0x10) = *(long *)(this + 0x10) + -1;
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
                    /* try { // try from 00afbfe8 to 00bfbfef has its CatchHandler @ 00b00380 */
      operator_delete(plVar7);
      lVar5 = *(long *)(this + 0x10);
                    /* try { // try from 00afbff0 to 00bfc0eb has its CatchHandler @ 00af560c */
    }
  }
  Mutex::Release(this_00);
  Mutex::~Mutex((Mutex *)(this + 0x40));
  Mutex::~Mutex(this_00);
  if (*(long *)(this + 0x10) != 0) {
    lVar5 = *(long *)this;
    pCVar2 = *(CallbackDispatcher **)(this + 8);
    lVar6 = *(long *)pCVar2;
    *(undefined8 *)(lVar6 + 8) = *(undefined8 *)(lVar5 + 8);
    **(long **)(lVar5 + 8) = lVar6;
    *(undefined8 *)(this + 0x10) = 0;
    while (pCVar2 != this) {
                    /* try { // try from 00afc0ec to 00bfc10f has its CatchHandler @ 00b00450 */
      p_Var8 = *(__shared_weak_count **)(pCVar2 + 0x18);
      pCVar9 = *(CallbackDispatcher **)(pCVar2 + 8);
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
                    /* try { // try from 00afc110 to 00bfc11b has its CatchHandler @ 00b003a4 */
          (**(code **)(*(long *)p_Var8 + 0x10))(p_Var8);
          std::__ndk1::__shared_weak_count::__release_weak(p_Var8);
        }
      }
      operator_delete(pCVar2);
      pCVar2 = pCVar9;
    }
  }
  return;
}

~~~
