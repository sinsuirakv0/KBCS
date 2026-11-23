# 00ae7ddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae7ea4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0059.md#compare-2a4be8f4e95620cbad5a99606f49adc3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae7ddc",
  "name": "_ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a3eedaf1dd24139df2d16dc3b428cba443ab54ad55426b31e79c05e2b3f3949",
  "source_text_sha256": "8a3eedaf1dd24139df2d16dc3b428cba443ab54ad55426b31e79c05e2b3f3949",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae7ddc",
        "00ae7e7b"
      ]
    ],
    "bytes_sha256": "132afd3538b71ce9453a8f9ed046636ed44b5ccc0e7bf85f9da21dfe2045a859",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 902 bytes

~~~c

void _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a04c0 != 0) {
                    /* try { // try from 00ae7df8 to 00be7e03 has its CatchHandler @ 00ae8c20 */
    if (DAT_010a04c8 != '\0') {
                    /* try { // try from 00ae7e08 to 00be7e17 has its CatchHandler @ 00ae8c1c */
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a04c8 = '\0';
    }
                    /* try { // try from 00ae7e1c to 00be7e2f has its CatchHandler @ 00ae8c08 */
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
                    /* try { // try from 00ae7e48 to 00be7e4f has its CatchHandler @ 00ae8bf0 */
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a04c0);
    DAT_010a04c0 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae7ddc"></a> `00ae7ddc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00ae7de0"></a> `00ae7de0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7de4"></a> `00ae7de4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae7de8"></a> `00ae7de8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ae7dec"></a> `00ae7dec` | `d4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7df0"></a> `00ae7df0` | `81 62 42 f9` | ldr x1,[x20, #0x4c0] | `FALL_THROUGH`
<a id="insn-00ae7df4"></a> `00ae7df4` | `c1 03 00 b4` | cbz x1,0x00ae7e6c | `CONDITIONAL_JUMP`
<a id="insn-00ae7df8"></a> `00ae7df8` | `d5 2d 00 b0` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae7dfc"></a> `00ae7dfc` | `a8 22 53 39` | ldrb w8,[x21, #0x4c8] | `FALL_THROUGH`
<a id="insn-00ae7e00"></a> `00ae7e00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae7e04"></a> `00ae7e04` | `c8 00 00 34` | cbz w8,0x00ae7e1c | `CONDITIONAL_JUMP`
<a id="insn-00ae7e08"></a> `00ae7e08` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7e0c"></a> `00ae7e0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7e10"></a> `00ae7e10` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00ae7e14"></a> `00ae7e14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7e18"></a> `00ae7e18` | `bf 22 13 39` | strb wzr,[x21, #0x4c8] | `FALL_THROUGH`
<a id="insn-00ae7e1c"></a> `00ae7e1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7e20"></a> `00ae7e20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7e24"></a> `00ae7e24` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00ae7e28"></a> `00ae7e28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7e2c"></a> `00ae7e2c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00ae7e30"></a> `00ae7e30` | `20 01 00 54` | b.eq 0x00ae7e54 | `CONDITIONAL_JUMP`
<a id="insn-00ae7e34"></a> `00ae7e34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7e38"></a> `00ae7e38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7e3c"></a> `00ae7e3c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00ae7e40"></a> `00ae7e40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7e44"></a> `00ae7e44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7e48"></a> `00ae7e48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7e4c"></a> `00ae7e4c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00ae7e50"></a> `00ae7e50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7e54"></a> `00ae7e54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ae7e58"></a> `00ae7e58` | `81 62 42 f9` | ldr x1,[x20, #0x4c0] | `FALL_THROUGH`
<a id="insn-00ae7e5c"></a> `00ae7e5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae7e60"></a> `00ae7e60` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00ae7e64"></a> `00ae7e64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ae7e68"></a> `00ae7e68` | `9f 62 02 f9` | str xzr,[x20, #0x4c0] | `FALL_THROUGH`
<a id="insn-00ae7e6c"></a> `00ae7e6c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae7e70"></a> `00ae7e70` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae7e74"></a> `00ae7e74` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00ae7e78"></a> `00ae7e78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae7ddc`](#insn-00ae7ddc) 範囲 `[['00ae7ddc', '00ae7df7']]`
  - `CONDITIONAL_JUMP` [`00ae7df4`](#insn-00ae7df4) → [`00ae7e6c`](#insn-00ae7e6c)
  - `FALL_THROUGH` [`00ae7df4`](#insn-00ae7df4) → [`00ae7df8`](#insn-00ae7df8)
- ブロック [`00ae7df8`](#insn-00ae7df8) 範囲 `[['00ae7df8', '00ae7e07']]`
  - `CONDITIONAL_JUMP` [`00ae7e04`](#insn-00ae7e04) → [`00ae7e1c`](#insn-00ae7e1c)
  - `FALL_THROUGH` [`00ae7e04`](#insn-00ae7e04) → [`00ae7e08`](#insn-00ae7e08)
- ブロック [`00ae7e08`](#insn-00ae7e08) 範囲 `[['00ae7e08', '00ae7e1b']]`
  - `FALL_THROUGH` [`00ae7e18`](#insn-00ae7e18) → [`00ae7e1c`](#insn-00ae7e1c)
- ブロック [`00ae7e1c`](#insn-00ae7e1c) 範囲 `[['00ae7e1c', '00ae7e33']]`
  - `CONDITIONAL_JUMP` [`00ae7e30`](#insn-00ae7e30) → [`00ae7e54`](#insn-00ae7e54)
  - `FALL_THROUGH` [`00ae7e30`](#insn-00ae7e30) → [`00ae7e34`](#insn-00ae7e34)
- ブロック [`00ae7e34`](#insn-00ae7e34) 範囲 `[['00ae7e34', '00ae7e47']]`
  - `FALL_THROUGH` [`00ae7e44`](#insn-00ae7e44) → [`00ae7e48`](#insn-00ae7e48)
- ブロック [`00ae7e48`](#insn-00ae7e48) 範囲 `[['00ae7e48', '00ae7e53']]`
  - `FALL_THROUGH` [`00ae7e50`](#insn-00ae7e50) → [`00ae7e54`](#insn-00ae7e54)
- ブロック [`00ae7e54`](#insn-00ae7e54) 範囲 `[['00ae7e54', '00ae7e6b']]`
  - `FALL_THROUGH` [`00ae7e68`](#insn-00ae7e68) → [`00ae7e6c`](#insn-00ae7e6c)
- ブロック [`00ae7e6c`](#insn-00ae7e6c) 範囲 `[['00ae7e6c', '00ae7e7b']]`

## 命令位置別の参照

- [`00ae7ddc`](#insn-00ae7ddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7de0`](#insn-00ae7de0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7de4`](#insn-00ae7de4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7df0`](#insn-00ae7df0) → `010a04c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7df4`](#insn-00ae7df4) → [`00ae7e6c`](#insn-00ae7e6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7dfc`](#insn-00ae7dfc) → `010a04c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae7e04`](#insn-00ae7e04) → [`00ae7e1c`](#insn-00ae7e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e18`](#insn-00ae7e18) → `010a04c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00ae7e30`](#insn-00ae7e30) → [`00ae7e54`](#insn-00ae7e54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e58`](#insn-00ae7e58) → `010a04c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7e68`](#insn-00ae7e68) → `010a04c0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae7e6c`](#insn-00ae7e6c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae7e70`](#insn-00ae7e70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae7ddc`](#insn-00ae7ddc)

~~~json
{
  "source": "00ae7ddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7de0`](#insn-00ae7de0)

~~~json
{
  "source": "00ae7de0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7de4`](#insn-00ae7de4)

~~~json
{
  "source": "00ae7de4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7df0`](#insn-00ae7df0)

~~~json
{
  "source": "00ae7df0",
  "target": "010a04c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7df4`](#insn-00ae7df4)

~~~json
{
  "source": "00ae7df4",
  "target": "00ae7e6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7dfc`](#insn-00ae7dfc)

~~~json
{
  "source": "00ae7dfc",
  "target": "010a04c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7e04`](#insn-00ae7e04)

~~~json
{
  "source": "00ae7e04",
  "target": "00ae7e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7e18`](#insn-00ae7e18)

~~~json
{
  "source": "00ae7e18",
  "target": "010a04c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7e30`](#insn-00ae7e30)

~~~json
{
  "source": "00ae7e30",
  "target": "00ae7e54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7e58`](#insn-00ae7e58)

~~~json
{
  "source": "00ae7e58",
  "target": "010a04c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7e68`](#insn-00ae7e68)

~~~json
{
  "source": "00ae7e68",
  "target": "010a04c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a04c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae7e6c`](#insn-00ae7e6c)

~~~json
{
  "source": "00ae7e6c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae7e70`](#insn-00ae7e70)

~~~json
{
  "source": "00ae7e70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
