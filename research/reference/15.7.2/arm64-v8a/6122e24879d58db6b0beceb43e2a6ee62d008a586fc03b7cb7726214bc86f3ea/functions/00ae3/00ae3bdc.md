# 00ae3bdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae3bdc.md)

## 関数情報

~~~json
{
  "address": "00ae3bdc",
  "name": "firebase::ReferenceCountedFutureImpl::CompleteInternal<int,firebase::ReferenceCountedFutureImpl::CompleteWithResultInternal<int>(firebase::FutureHandle_const&,int,char_const*,int_const&)::{lambda(int*)#1}>",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38cc2081ba35265904f8144094fe21def44001401b5bf9c7bef0c219fb70f1c1",
  "source_text_sha256": "38cc2081ba35265904f8144094fe21def44001401b5bf9c7bef0c219fb70f1c1"
}
~~~
## 呼び出し元

- [00bdde10](../00bdd/00bdde10.md)

## 呼び出し先

- [00bddb20](../00bdd/00bddb20.md)
- [00bddb30](../00bdd/00bddb30.md)
- [00bddeb0](../00bdd/00bddeb0.md)
- [00bdded0](../00bdd/00bdded0.md)
- [00bddee0](../00bdd/00bddee0.md)
- [00bddef0](../00bdd/00bddef0.md)
- [00bddf00](../00bdd/00bddf00.md)
- [00bddf10](../00bdd/00bddf10.md)
- [00bde080](../00bde/00bde080.md)
- [00bde0f0](../00bde/00bde0f0.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~
## 疑似コード 1/1 / UTF-8 2378 bytes

~~~c

/* void firebase::ReferenceCountedFutureImpl::CompleteInternal<int,
   firebase::ReferenceCountedFutureImpl::CompleteWithResultInternal<int>(firebase::FutureHandle
   const&, int, char const*, int const&)::{lambda(int*)#1}>(firebase::FutureHandle const&, int, char
   const*,
   firebase::ReferenceCountedFutureImpl::CompleteWithResultInternal<int>(firebase::FutureHandle
   const&, int, char const*, int const&)::{lambda(int*)#1} const&) */

void __thiscall
firebase::ReferenceCountedFutureImpl::
CompleteInternal<int,firebase::ReferenceCountedFutureImpl::CompleteWithResultInternal<int>(firebase::FutureHandle_const&,int,char_const*,int_const&)::_lambda(int*)_1_>
          (ReferenceCountedFutureImpl *this,FutureHandle *param_1,int param_2,char *param_3,
          _lambda_int___1_ *param_4)

{
  int iVar1;
  FutureBackingData *pFVar2;
  undefined4 *puVar3;
  ulong uVar4;
  
  Mutex::Acquire((Mutex *)(this + 8));
  pFVar2 = (FutureBackingData *)BackingFromHandle(this,*(ulong *)param_1);
  if (pFVar2 == (FutureBackingData *)0x0) {
    Mutex::Release((Mutex *)(this + 8));
    return;
  }
  iVar1 = (**(code **)(*(long *)this + 0x20))(this,param_1);
  if (iVar1 != 1) {
    LogAssert("GetFutureStatus(handle) == kFutureStatusPending");
  }
                    /* try { // try from 00ae3c58 to 00be3c9f has its CatchHandler @ 00ae3c58
                       catch() { ... } // from try @ 00ae3c58 with catch @ 00ae3c58
                       catch() { ... } // from try @ 00ae3cac with catch @ 00ae3c58 */
  SetBackingError(this,pFVar2,param_2,param_3);
  puVar3 = (undefined4 *)BackingData(this,pFVar2);
  *puVar3 = *(undefined4 *)param_4;
  CompleteHandle(this,param_1);
  CompleteProxy(this,pFVar2);
  ReleaseMutexAndRunCallbacks(this,param_1);
                    /* try { // try from 00ae3ca0 to 00be3cab has its CatchHandler @ 00ae3cfc */
  uVar4 = is_orphaned(this);
  if ((uVar4 & 1) != 0) {
                    /* try { // try from 00ae3cac to 00be3d4b has its CatchHandler @ 00ae3c58 */
                    /* WARNING: Could not recover jumptable at 0x00ae3cc8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*(long *)this + 8))(this);
    return;
  }
                    /* catch() { ... } // from try @ 00ae3ca0 with catch @ 00ae3cfc */
  return;
}

~~~
