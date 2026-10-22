# 00bdece0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdece0.md)

## 関数情報

~~~json
{
  "address": "00bdece0",
  "name": "firebase::ReferenceCountedFutureImpl::SetContextData",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56abff88beabd785a8925dcacad493775c99b859035b5cceb9e558e55cdaaa39",
  "source_text_sha256": "56abff88beabd785a8925dcacad493775c99b859035b5cceb9e558e55cdaaa39"
}
~~~
## 呼び出し元

- [00b00570](../00b00/00b00570.md)

## 呼び出し先

- [00b004b0](../00b00/00b004b0.md)

## 疑似コード 1/1 / UTF-8 262 bytes

~~~c

void __thiscall
firebase::ReferenceCountedFutureImpl::SetContextData
          (ReferenceCountedFutureImpl *this,FutureHandle *param_1,void *param_2,
          _func_void_void_ptr *param_3)

{
  (*(code *)PTR_SetContextData_00c1dea8)();
  return;
}

~~~
