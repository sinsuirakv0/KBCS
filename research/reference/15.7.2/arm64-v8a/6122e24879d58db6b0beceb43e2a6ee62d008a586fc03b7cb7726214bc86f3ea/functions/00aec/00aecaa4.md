# 00aecaa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecb6c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-867e5a7d332169d81777c5b5e54f23c3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecaa4",
  "name": "_ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1054a99ff487b417f60624aa848bc4003c8d135c306c9db2902a5de03d41b8b6",
  "source_text_sha256": "1054a99ff487b417f60624aa848bc4003c8d135c306c9db2902a5de03d41b8b6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecaa4",
        "00aecb43"
      ]
    ],
    "bytes_sha256": "64aae32e569b06f8f3c537f8d67963bf780dfd097446909c22535fc684fc3b57",
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

## 疑似コード / UTF-8 717 bytes

~~~c

void _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a08a8 != 0) {
                    /* try { // try from 00aecacc to 00becad7 has its CatchHandler @ 00af1898 */
    if (DAT_010a08b0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a08b0 = '\0';
    }
                    /* try { // try from 00aecae8 to 00becaef has its CatchHandler @ 00af1a38 */
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a08a8);
    DAT_010a08a8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecaa4"></a> `00aecaa4` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aecaa8"></a> `00aecaa8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecaac"></a> `00aecaac` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecab0"></a> `00aecab0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecab4"></a> `00aecab4` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecab8"></a> `00aecab8` | `81 56 44 f9` | ldr x1,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00aecabc"></a> `00aecabc` | `c1 03 00 b4` | cbz x1,0x00aecb34 | `CONDITIONAL_JUMP`
<a id="insn-00aecac0"></a> `00aecac0` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecac4"></a> `00aecac4` | `a8 c2 62 39` | ldrb w8,[x21, #0x8b0] | `FALL_THROUGH`
<a id="insn-00aecac8"></a> `00aecac8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecacc"></a> `00aecacc` | `c8 00 00 34` | cbz w8,0x00aecae4 | `CONDITIONAL_JUMP`
<a id="insn-00aecad0"></a> `00aecad0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecad4"></a> `00aecad4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecad8"></a> `00aecad8` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aecadc"></a> `00aecadc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecae0"></a> `00aecae0` | `bf c2 22 39` | strb wzr,[x21, #0x8b0] | `FALL_THROUGH`
<a id="insn-00aecae4"></a> `00aecae4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecae8"></a> `00aecae8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecaec"></a> `00aecaec` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aecaf0"></a> `00aecaf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecaf4"></a> `00aecaf4` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aecaf8"></a> `00aecaf8` | `20 01 00 54` | b.eq 0x00aecb1c | `CONDITIONAL_JUMP`
<a id="insn-00aecafc"></a> `00aecafc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb00"></a> `00aecb00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb04"></a> `00aecb04` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aecb08"></a> `00aecb08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb0c"></a> `00aecb0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb10"></a> `00aecb10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb14"></a> `00aecb14` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aecb18"></a> `00aecb18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb1c"></a> `00aecb1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecb20"></a> `00aecb20` | `81 56 44 f9` | ldr x1,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00aecb24"></a> `00aecb24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecb28"></a> `00aecb28` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aecb2c"></a> `00aecb2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecb30"></a> `00aecb30` | `9f 56 04 f9` | str xzr,[x20, #0x8a8] | `FALL_THROUGH`
<a id="insn-00aecb34"></a> `00aecb34` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecb38"></a> `00aecb38` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecb3c"></a> `00aecb3c` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aecb40"></a> `00aecb40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecaa4`](#insn-00aecaa4) 範囲 `[['00aecaa4', '00aecabf']]`
  - `CONDITIONAL_JUMP` [`00aecabc`](#insn-00aecabc) → [`00aecb34`](#insn-00aecb34)
  - `FALL_THROUGH` [`00aecabc`](#insn-00aecabc) → [`00aecac0`](#insn-00aecac0)
- ブロック [`00aecac0`](#insn-00aecac0) 範囲 `[['00aecac0', '00aecacb']]`
  - `FALL_THROUGH` [`00aecac8`](#insn-00aecac8) → [`00aecacc`](#insn-00aecacc)
- ブロック [`00aecacc`](#insn-00aecacc) 範囲 `[['00aecacc', '00aecacf']]`
  - `CONDITIONAL_JUMP` [`00aecacc`](#insn-00aecacc) → [`00aecae4`](#insn-00aecae4)
  - `FALL_THROUGH` [`00aecacc`](#insn-00aecacc) → [`00aecad0`](#insn-00aecad0)
- ブロック [`00aecad0`](#insn-00aecad0) 範囲 `[['00aecad0', '00aecae3']]`
  - `FALL_THROUGH` [`00aecae0`](#insn-00aecae0) → [`00aecae4`](#insn-00aecae4)
- ブロック [`00aecae4`](#insn-00aecae4) 範囲 `[['00aecae4', '00aecae7']]`
  - `FALL_THROUGH` [`00aecae4`](#insn-00aecae4) → [`00aecae8`](#insn-00aecae8)
- ブロック [`00aecae8`](#insn-00aecae8) 範囲 `[['00aecae8', '00aecafb']]`
  - `CONDITIONAL_JUMP` [`00aecaf8`](#insn-00aecaf8) → [`00aecb1c`](#insn-00aecb1c)
  - `FALL_THROUGH` [`00aecaf8`](#insn-00aecaf8) → [`00aecafc`](#insn-00aecafc)
- ブロック [`00aecafc`](#insn-00aecafc) 範囲 `[['00aecafc', '00aecb1b']]`
  - `FALL_THROUGH` [`00aecb18`](#insn-00aecb18) → [`00aecb1c`](#insn-00aecb1c)
- ブロック [`00aecb1c`](#insn-00aecb1c) 範囲 `[['00aecb1c', '00aecb33']]`
  - `FALL_THROUGH` [`00aecb30`](#insn-00aecb30) → [`00aecb34`](#insn-00aecb34)
- ブロック [`00aecb34`](#insn-00aecb34) 範囲 `[['00aecb34', '00aecb43']]`

## 命令位置別の参照

- [`00aecaa4`](#insn-00aecaa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecaa8`](#insn-00aecaa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecaac`](#insn-00aecaac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecab8`](#insn-00aecab8) → `010a08a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecabc`](#insn-00aecabc) → [`00aecb34`](#insn-00aecb34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecac4`](#insn-00aecac4) → `010a08b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecacc`](#insn-00aecacc) → [`00aecae4`](#insn-00aecae4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecae0`](#insn-00aecae0) → `010a08b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecaf8`](#insn-00aecaf8) → [`00aecb1c`](#insn-00aecb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb20`](#insn-00aecb20) → `010a08a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecb30`](#insn-00aecb30) → `010a08a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecb34`](#insn-00aecb34) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecb38`](#insn-00aecb38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecaa4`](#insn-00aecaa4)

~~~json
{
  "source": "00aecaa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecaa8`](#insn-00aecaa8)

~~~json
{
  "source": "00aecaa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecaac`](#insn-00aecaac)

~~~json
{
  "source": "00aecaac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecab8`](#insn-00aecab8)

~~~json
{
  "source": "00aecab8",
  "target": "010a08a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecabc`](#insn-00aecabc)

~~~json
{
  "source": "00aecabc",
  "target": "00aecb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecac4`](#insn-00aecac4)

~~~json
{
  "source": "00aecac4",
  "target": "010a08b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecacc`](#insn-00aecacc)

~~~json
{
  "source": "00aecacc",
  "target": "00aecae4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecae0`](#insn-00aecae0)

~~~json
{
  "source": "00aecae0",
  "target": "010a08b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08b0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecaf8`](#insn-00aecaf8)

~~~json
{
  "source": "00aecaf8",
  "target": "00aecb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb20`](#insn-00aecb20)

~~~json
{
  "source": "00aecb20",
  "target": "010a08a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecb30`](#insn-00aecb30)

~~~json
{
  "source": "00aecb30",
  "target": "010a08a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecb34`](#insn-00aecb34)

~~~json
{
  "source": "00aecb34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecb38`](#insn-00aecb38)

~~~json
{
  "source": "00aecb38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
