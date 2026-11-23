# 00aeabd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeab08`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeab08.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-bd05c455a5eb974f6607e8979fef8871)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeac14`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-b5cca57145c89ec5d20848c4424e1400)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeabd0",
  "name": "_ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9a0b2012c6cf57fee1433e8920629465f8c026e2659c5ac204290968707e7c18",
  "source_text_sha256": "9a0b2012c6cf57fee1433e8920629465f8c026e2659c5ac204290968707e7c18",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeabd0",
        "00aeac3f"
      ]
    ],
    "bytes_sha256": "22ab9fae6dbb6ecf98634a1daa113ea8d882b80bd206c037881d009975e9200b",
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

- [00bde020](../00bde/00bde020.md)
- [00bde040](../00bde/00bde040.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Float"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 689 bytes

~~~c

void _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a07e8 == 0) {
    DAT_010a07e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Float",0);
  }
                    /* try { // try from 00aeac14 to 00beadc7 has its CatchHandler @ 00aeaa38 */
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a07e8,&DAT_002f5cb0,1,&DAT_010a0808,"java/lang/Float");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeabd0"></a> `00aeabd0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeabd4"></a> `00aeabd4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeabd8"></a> `00aeabd8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeabdc"></a> `00aeabdc` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeabe0"></a> `00aeabe0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeabe4"></a> `00aeabe4` | `81 f6 43 f9` | ldr x1,[x20, #0x7e8] | `FALL_THROUGH`
<a id="insn-00aeabe8"></a> `00aeabe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeabec"></a> `00aeabec` | `41 01 00 b5` | cbnz x1,0x00aeac14 | `CONDITIONAL_JUMP`
<a id="insn-00aeabf0"></a> `00aeabf0` | `63 bd ff f0` | adrp x3,0x299000 | `FALL_THROUGH`
<a id="insn-00aeabf4"></a> `00aeabf4` | `63 84 1b 91` | add x3,x3,#0x6e1 | `FALL_THROUGH`
<a id="insn-00aeabf8"></a> `00aeabf8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeabfc"></a> `00aeabfc` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeac00"></a> `00aeac00` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeac04"></a> `00aeac04` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeac08"></a> `00aeac08` | `0e cd 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeac0c"></a> `00aeac0c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeac10"></a> `00aeac10` | `80 f6 03 f9` | str x0,[x20, #0x7e8] | `FALL_THROUGH`
<a id="insn-00aeac14"></a> `00aeac14` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeac18"></a> `00aeac18` | `42 c0 ff f0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aeac1c"></a> `00aeac1c` | `a4 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeac20"></a> `00aeac20` | `65 bd ff f0` | adrp x5,0x299000 | `FALL_THROUGH`
<a id="insn-00aeac24"></a> `00aeac24` | `42 c0 32 91` | add x2,x2,#0xcb0 | `FALL_THROUGH`
<a id="insn-00aeac28"></a> `00aeac28` | `84 20 20 91` | add x4,x4,#0x808 | `FALL_THROUGH`
<a id="insn-00aeac2c"></a> `00aeac2c` | `a5 84 1b 91` | add x5,x5,#0x6e1 | `FALL_THROUGH`
<a id="insn-00aeac30"></a> `00aeac30` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aeac34"></a> `00aeac34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeac38"></a> `00aeac38` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeac3c"></a> `00aeac3c` | `f9 cc 03 14` | b 0x00bde020 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeabd0`](#insn-00aeabd0) 範囲 `[['00aeabd0', '00aeabef']]`
  - `CONDITIONAL_JUMP` [`00aeabec`](#insn-00aeabec) → [`00aeac14`](#insn-00aeac14)
  - `FALL_THROUGH` [`00aeabec`](#insn-00aeabec) → [`00aeabf0`](#insn-00aeabf0)
- ブロック [`00aeabf0`](#insn-00aeabf0) 範囲 `[['00aeabf0', '00aeac13']]`
  - `FALL_THROUGH` [`00aeac10`](#insn-00aeac10) → [`00aeac14`](#insn-00aeac14)
- ブロック [`00aeac14`](#insn-00aeac14) 範囲 `[['00aeac14', '00aeac3f']]`

## 命令位置別の参照

- [`00aeabd0`](#insn-00aeabd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabd4`](#insn-00aeabd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabe4`](#insn-00aeabe4) → `010a07e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeabec`](#insn-00aeabec) → [`00aeac14`](#insn-00aeac14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeabf4`](#insn-00aeabf4) → `002996e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeac08`](#insn-00aeac08) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeac10`](#insn-00aeac10) → `010a07e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeac14`](#insn-00aeac14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac24`](#insn-00aeac24) → `002f5cb0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac28`](#insn-00aeac28) → `010a0808`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeac2c`](#insn-00aeac2c) → `002996e1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeac3c`](#insn-00aeac3c) → [`00bde020`](../00bde/00bde020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde020` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeabd0`](#insn-00aeabd0)

~~~json
{
  "source": "00aeabd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabd4`](#insn-00aeabd4)

~~~json
{
  "source": "00aeabd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabe4`](#insn-00aeabe4)

~~~json
{
  "source": "00aeabe4",
  "target": "010a07e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeabec`](#insn-00aeabec)

~~~json
{
  "source": "00aeabec",
  "target": "00aeac14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeabf4`](#insn-00aeabf4)

~~~json
{
  "source": "00aeabf4",
  "target": "002996e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002996e1",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f466c6f617400",
  "capture_start": "002996e1",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeac08`](#insn-00aeac08)

~~~json
{
  "source": "00aeac08",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeac10`](#insn-00aeac10)

~~~json
{
  "source": "00aeac10",
  "target": "010a07e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a07e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeac14`](#insn-00aeac14)

~~~json
{
  "source": "00aeac14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac24`](#insn-00aeac24)

~~~json
{
  "source": "00aeac24",
  "target": "002f5cb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac28`](#insn-00aeac28)

~~~json
{
  "source": "00aeac28",
  "target": "010a0808",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeac2c`](#insn-00aeac2c)

~~~json
{
  "source": "00aeac2c",
  "target": "002996e1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002996e1",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f466c6f617400",
  "capture_start": "002996e1",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeac3c`](#insn-00aeac3c)

~~~json
{
  "source": "00aeac3c",
  "target": "00bde020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
