# 00bdcc8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d78c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d78c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-5ab1656d668ddde444fe042159506dd8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd0b4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd0b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-60077a673d52c638e66fb4a8b730090b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcc8c",
  "name": "_ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f44c943580cf4642f561bd60f8dcab48f852a6cc49d0d629195741a3ab7148b",
  "source_text_sha256": "4f44c943580cf4642f561bd60f8dcab48f852a6cc49d0d629195741a3ab7148b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcc8c",
        "00bdccfb"
      ]
    ],
    "bytes_sha256": "b83e267b27cba7afa5b0163d4b5913eaf1e329024827633b4e4769c38430dbe2",
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

- [00c5aaf0](../00c5a/00c5aaf0.md)
- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 654 bytes

~~~c

void _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126900 == 0) {
    DAT_01126900 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01126900,&DAT_00310190,1,&DAT_01126918,
             "com/google/firebase/auth/GetTokenResult");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcc8c"></a> `00bdcc8c` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcc90"></a> `00bdcc90` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcc94"></a> `00bdcc94` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcc98"></a> `00bdcc98` | `54 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcc9c"></a> `00bdcc9c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdcca0"></a> `00bdcca0` | `81 82 44 f9` | ldr x1,[x20, #0x900] | `FALL_THROUGH`
<a id="insn-00bdcca4"></a> `00bdcca4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcca8"></a> `00bdcca8` | `41 01 00 b5` | cbnz x1,0x00bdccd0 | `CONDITIONAL_JUMP`
<a id="insn-00bdccac"></a> `00bdccac` | `03 b7 ff 90` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdccb0"></a> `00bdccb0` | `63 40 08 91` | add x3,x3,#0x210 | `FALL_THROUGH`
<a id="insn-00bdccb4"></a> `00bdccb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdccb8"></a> `00bdccb8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdccbc"></a> `00bdccbc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdccc0"></a> `00bdccc0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdccc4"></a> `00bdccc4` | `93 f7 01 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdccc8"></a> `00bdccc8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdcccc"></a> `00bdcccc` | `80 82 04 f9` | str x0,[x20, #0x900] | `FALL_THROUGH`
<a id="insn-00bdccd0"></a> `00bdccd0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdccd4"></a> `00bdccd4` | `a2 b9 ff 90` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bdccd8"></a> `00bdccd8` | `44 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdccdc"></a> `00bdccdc` | `05 b7 ff 90` | adrp x5,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdcce0"></a> `00bdcce0` | `42 40 06 91` | add x2,x2,#0x190 | `FALL_THROUGH`
<a id="insn-00bdcce4"></a> `00bdcce4` | `84 60 24 91` | add x4,x4,#0x918 | `FALL_THROUGH`
<a id="insn-00bdcce8"></a> `00bdcce8` | `a5 40 08 91` | add x5,x5,#0x210 | `FALL_THROUGH`
<a id="insn-00bdccec"></a> `00bdccec` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdccf0"></a> `00bdccf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdccf4"></a> `00bdccf4` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdccf8"></a> `00bdccf8` | `7e f7 01 14` | b 0x00c5aaf0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcc8c`](#insn-00bdcc8c) 範囲 `[['00bdcc8c', '00bdccab']]`
  - `CONDITIONAL_JUMP` [`00bdcca8`](#insn-00bdcca8) → [`00bdccd0`](#insn-00bdccd0)
  - `FALL_THROUGH` [`00bdcca8`](#insn-00bdcca8) → [`00bdccac`](#insn-00bdccac)
- ブロック [`00bdccac`](#insn-00bdccac) 範囲 `[['00bdccac', '00bdcccf']]`
  - `FALL_THROUGH` [`00bdcccc`](#insn-00bdcccc) → [`00bdccd0`](#insn-00bdccd0)
- ブロック [`00bdccd0`](#insn-00bdccd0) 範囲 `[['00bdccd0', '00bdccfb']]`

## 命令位置別の参照

- [`00bdcc8c`](#insn-00bdcc8c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc90`](#insn-00bdcc90) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcca0`](#insn-00bdcca0) → `01126900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcca8`](#insn-00bdcca8) → [`00bdccd0`](#insn-00bdccd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccb0`](#insn-00bdccb0) → `002bc210`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdccc4`](#insn-00bdccc4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bdcccc`](#insn-00bdcccc) → `01126900`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdccd0`](#insn-00bdccd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcce0`](#insn-00bdcce0) → `00310190`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcce4`](#insn-00bdcce4) → `01126918`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcce8`](#insn-00bdcce8) → `002bc210`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdccf8`](#insn-00bdccf8) → [`00c5aaf0`](../00c5a/00c5aaf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aaf0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcc8c`](#insn-00bdcc8c)

~~~json
{
  "source": "00bdcc8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc90`](#insn-00bdcc90)

~~~json
{
  "source": "00bdcc90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcca0`](#insn-00bdcca0)

~~~json
{
  "source": "00bdcca0",
  "target": "01126900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcca8`](#insn-00bdcca8)

~~~json
{
  "source": "00bdcca8",
  "target": "00bdccd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccb0`](#insn-00bdccb0)

~~~json
{
  "source": "00bdccb0",
  "target": "002bc210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc20c",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc20c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdccc4`](#insn-00bdccc4)

~~~json
{
  "source": "00bdccc4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcccc`](#insn-00bdcccc)

~~~json
{
  "source": "00bdcccc",
  "target": "01126900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdccd0`](#insn-00bdccd0)

~~~json
{
  "source": "00bdccd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcce0`](#insn-00bdcce0)

~~~json
{
  "source": "00bdcce0",
  "target": "00310190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcce4`](#insn-00bdcce4)

~~~json
{
  "source": "00bdcce4",
  "target": "01126918",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcce8`](#insn-00bdcce8)

~~~json
{
  "source": "00bdcce8",
  "target": "002bc210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc20c",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc20c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdccf8`](#insn-00bdccf8)

~~~json
{
  "source": "00bdccf8",
  "target": "00c5aaf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
