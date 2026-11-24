# 00b4cfec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4bff8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bff8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0075.md#compare-f58919ad7dc0a54a07a3a332543d97f7)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cfec",
  "name": "_ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a942bf6bc65ea87f0a7b4151350d289523e6ca63d66e98f148597186e704139d",
  "source_text_sha256": "a942bf6bc65ea87f0a7b4151350d289523e6ca63d66e98f148597186e704139d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4cfec",
        "00b4d05b"
      ]
    ],
    "bytes_sha256": "4e101111c4780fb58669710d3be6e9ec306d0c40f833b34f9030760de5342f02",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Iterator"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 612 bytes

~~~c

void _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126c78 == 0) {
    DAT_01126c78 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Iterator",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126c78,&PTR_s_hasNext_00c91050,2,&DAT_01126c88,"java/util/Iterator");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4cfec"></a> `00b4cfec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4cff0"></a> `00b4cff0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4cff4"></a> `00b4cff4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4cff8"></a> `00b4cff8` | `d4 2e 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4cffc"></a> `00b4cffc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b4d000"></a> `00b4d000` | `81 3e 46 f9` | ldr x1,[x20, #0xc78] | `FALL_THROUGH`
<a id="insn-00b4d004"></a> `00b4d004` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4d008"></a> `00b4d008` | `41 01 00 b5` | cbnz x1,0x00b4d030 | `CONDITIONAL_JUMP`
<a id="insn-00b4d00c"></a> `00b4d00c` | `c3 ba ff d0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00b4d010"></a> `00b4d010` | `63 4c 09 91` | add x3,x3,#0x253 | `FALL_THROUGH`
<a id="insn-00b4d014"></a> `00b4d014` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4d018"></a> `00b4d018` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b4d01c"></a> `00b4d01c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b4d020"></a> `00b4d020` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4d024"></a> `00b4d024` | `e3 3b 04 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b4d028"></a> `00b4d028` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b4d02c"></a> `00b4d02c` | `80 3e 06 f9` | str x0,[x20, #0xc78] | `FALL_THROUGH`
<a id="insn-00b4d030"></a> `00b4d030` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4d034"></a> `00b4d034` | `22 0a 00 90` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00b4d038"></a> `00b4d038` | `c4 2e 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00b4d03c"></a> `00b4d03c` | `c5 ba ff d0` | adrp x5,0x2a7000 | `FALL_THROUGH`
<a id="insn-00b4d040"></a> `00b4d040` | `42 40 01 91` | add x2,x2,#0x50 | `FALL_THROUGH`
<a id="insn-00b4d044"></a> `00b4d044` | `84 20 32 91` | add x4,x4,#0xc88 | `FALL_THROUGH`
<a id="insn-00b4d048"></a> `00b4d048` | `a5 4c 09 91` | add x5,x5,#0x253 | `FALL_THROUGH`
<a id="insn-00b4d04c"></a> `00b4d04c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00b4d050"></a> `00b4d050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4d054"></a> `00b4d054` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4d058"></a> `00b4d058` | `de 3b 04 14` | b 0x00c5bfd0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4cfec`](#insn-00b4cfec) 範囲 `[['00b4cfec', '00b4d00b']]`
  - `CONDITIONAL_JUMP` [`00b4d008`](#insn-00b4d008) → [`00b4d030`](#insn-00b4d030)
  - `FALL_THROUGH` [`00b4d008`](#insn-00b4d008) → [`00b4d00c`](#insn-00b4d00c)
- ブロック [`00b4d00c`](#insn-00b4d00c) 範囲 `[['00b4d00c', '00b4d02f']]`
  - `FALL_THROUGH` [`00b4d02c`](#insn-00b4d02c) → [`00b4d030`](#insn-00b4d030)
- ブロック [`00b4d030`](#insn-00b4d030) 範囲 `[['00b4d030', '00b4d05b']]`

## 命令位置別の参照

- [`00b4cfec`](#insn-00b4cfec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4cff0`](#insn-00b4cff0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4d000`](#insn-00b4d000) → `01126c78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4d008`](#insn-00b4d008) → [`00b4d030`](#insn-00b4d030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4d010`](#insn-00b4d010) → `002a7253`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4d024`](#insn-00b4d024) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00b4d02c`](#insn-00b4d02c) → `01126c78`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4d030`](#insn-00b4d030) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4d040`](#insn-00b4d040) → `00c91050`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b4d044`](#insn-00b4d044) → `01126c88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4d048`](#insn-00b4d048) → `002a7253`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4d058`](#insn-00b4d058) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4cfec`](#insn-00b4cfec)

~~~json
{
  "source": "00b4cfec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4cff0`](#insn-00b4cff0)

~~~json
{
  "source": "00b4cff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4d000`](#insn-00b4d000)

~~~json
{
  "source": "00b4d000",
  "target": "01126c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4d008`](#insn-00b4d008)

~~~json
{
  "source": "00b4d008",
  "target": "00b4d030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4d010`](#insn-00b4d010)

~~~json
{
  "source": "00b4d010",
  "target": "002a7253",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7253",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002a7253",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4d024`](#insn-00b4d024)

~~~json
{
  "source": "00b4d024",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4d02c`](#insn-00b4d02c)

~~~json
{
  "source": "00b4d02c",
  "target": "01126c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4d030`](#insn-00b4d030)

~~~json
{
  "source": "00b4d030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4d040`](#insn-00b4d040)

~~~json
{
  "source": "00b4d040",
  "target": "00c91050",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91050",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b4d044`](#insn-00b4d044)

~~~json
{
  "source": "00b4d044",
  "target": "01126c88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4d048`](#insn-00b4d048)

~~~json
{
  "source": "00b4d048",
  "target": "002a7253",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7253",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4974657261746f7200",
  "capture_start": "002a7253",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4d058`](#insn-00b4d058)

~~~json
{
  "source": "00b4d058",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
