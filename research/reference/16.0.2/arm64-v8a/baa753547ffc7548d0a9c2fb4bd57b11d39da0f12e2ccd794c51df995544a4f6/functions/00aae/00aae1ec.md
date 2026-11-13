# 00aae1ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aae1ec",
  "name": "FUN_00aae1ec",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a71cfc6bcaf16474761eb200bbcb20d3f936234a1ffcf1fd4e2836bd3f78c903",
  "source_text_sha256": "a71cfc6bcaf16474761eb200bbcb20d3f936234a1ffcf1fd4e2836bd3f78c903"
}
~~~

## 呼び出し元

- [00aa5998](../00aa5/00aa5998.md)
- [00aa6150](../00aa6/00aa6150.md)
- [00aae1ec](../00aae/00aae1ec.md)

## 呼び出し先

- [005b9f24](../005b9/005b9f24.md)
- [00aae1ec](../00aae/00aae1ec.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00aae1ec(undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
    FUN_00aae1ec(param_1,*param_2);
    FUN_00aae1ec(param_1,param_2[1]);
    FUN_005b9f24(param_2 + 5,param_2[6]);
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~
