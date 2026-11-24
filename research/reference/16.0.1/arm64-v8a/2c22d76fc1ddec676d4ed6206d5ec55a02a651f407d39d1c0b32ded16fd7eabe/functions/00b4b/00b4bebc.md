# 00b4bebc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4ba94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4ba94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0072.md#compare-6e84150a9dc18acec83ee07cc1822628)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b4bf58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bf58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0073.md#compare-f0f663e5552a0c691eb11e94bd9cb565)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4bebc",
  "name": "_ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b84e0cfa38b52ebadc8f55c850ceb382a67290439ace40d7817b6dda4d23ee3",
  "source_text_sha256": "9b84e0cfa38b52ebadc8f55c850ceb382a67290439ace40d7817b6dda4d23ee3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4bebc",
        "00b4bf5b"
      ]
    ],
    "bytes_sha256": "c703cd65b665bdd9b113f679a9a9322579d8f1bdd98bc1bdea59cf3d254d9eeb",
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

## 疑似コード / UTF-8 508 bytes

~~~c

void _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_01125bb8 != 0) {
    if (DAT_01125bc0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_01125bc0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_01125bb8);
    DAT_01125bb8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4bebc"></a> `00b4bebc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b4bec0"></a> `00b4bec0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bec4"></a> `00b4bec4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4bec8"></a> `00b4bec8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b4becc"></a> `00b4becc` | `d4 2e 00 d0` | adrp x20,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bed0"></a> `00b4bed0` | `81 de 45 f9` | ldr x1,[x20, #0xbb8] | `FALL_THROUGH`
<a id="insn-00b4bed4"></a> `00b4bed4` | `c1 03 00 b4` | cbz x1,0x00b4bf4c | `CONDITIONAL_JUMP`
<a id="insn-00b4bed8"></a> `00b4bed8` | `d5 2e 00 d0` | adrp x21,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bedc"></a> `00b4bedc` | `a8 02 6f 39` | ldrb w8,[x21, #0xbc0] | `FALL_THROUGH`
<a id="insn-00b4bee0"></a> `00b4bee0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b4bee4"></a> `00b4bee4` | `c8 00 00 34` | cbz w8,0x00b4befc | `CONDITIONAL_JUMP`
<a id="insn-00b4bee8"></a> `00b4bee8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4beec"></a> `00b4beec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bef0"></a> `00b4bef0` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00b4bef4"></a> `00b4bef4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bef8"></a> `00b4bef8` | `bf 02 2f 39` | strb wzr,[x21, #0xbc0] | `FALL_THROUGH`
<a id="insn-00b4befc"></a> `00b4befc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf00"></a> `00b4bf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf04"></a> `00b4bf04` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00b4bf08"></a> `00b4bf08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf0c"></a> `00b4bf0c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00b4bf10"></a> `00b4bf10` | `20 01 00 54` | b.eq 0x00b4bf34 | `CONDITIONAL_JUMP`
<a id="insn-00b4bf14"></a> `00b4bf14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf18"></a> `00b4bf18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf1c"></a> `00b4bf1c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00b4bf20"></a> `00b4bf20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf24"></a> `00b4bf24` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf28"></a> `00b4bf28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf2c"></a> `00b4bf2c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00b4bf30"></a> `00b4bf30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf34"></a> `00b4bf34` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b4bf38"></a> `00b4bf38` | `81 de 45 f9` | ldr x1,[x20, #0xbb8] | `FALL_THROUGH`
<a id="insn-00b4bf3c"></a> `00b4bf3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b4bf40"></a> `00b4bf40` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00b4bf44"></a> `00b4bf44` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b4bf48"></a> `00b4bf48` | `9f de 05 f9` | str xzr,[x20, #0xbb8] | `FALL_THROUGH`
<a id="insn-00b4bf4c"></a> `00b4bf4c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b4bf50"></a> `00b4bf50` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bf54"></a> `00b4bf54` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b4bf58"></a> `00b4bf58` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4bebc`](#insn-00b4bebc) 範囲 `[['00b4bebc', '00b4bed7']]`
  - `CONDITIONAL_JUMP` [`00b4bed4`](#insn-00b4bed4) → [`00b4bf4c`](#insn-00b4bf4c)
  - `FALL_THROUGH` [`00b4bed4`](#insn-00b4bed4) → [`00b4bed8`](#insn-00b4bed8)
- ブロック [`00b4bed8`](#insn-00b4bed8) 範囲 `[['00b4bed8', '00b4bee7']]`
  - `CONDITIONAL_JUMP` [`00b4bee4`](#insn-00b4bee4) → [`00b4befc`](#insn-00b4befc)
  - `FALL_THROUGH` [`00b4bee4`](#insn-00b4bee4) → [`00b4bee8`](#insn-00b4bee8)
- ブロック [`00b4bee8`](#insn-00b4bee8) 範囲 `[['00b4bee8', '00b4befb']]`
  - `FALL_THROUGH` [`00b4bef8`](#insn-00b4bef8) → [`00b4befc`](#insn-00b4befc)
- ブロック [`00b4befc`](#insn-00b4befc) 範囲 `[['00b4befc', '00b4bf13']]`
  - `CONDITIONAL_JUMP` [`00b4bf10`](#insn-00b4bf10) → [`00b4bf34`](#insn-00b4bf34)
  - `FALL_THROUGH` [`00b4bf10`](#insn-00b4bf10) → [`00b4bf14`](#insn-00b4bf14)
- ブロック [`00b4bf14`](#insn-00b4bf14) 範囲 `[['00b4bf14', '00b4bf33']]`
  - `FALL_THROUGH` [`00b4bf30`](#insn-00b4bf30) → [`00b4bf34`](#insn-00b4bf34)
- ブロック [`00b4bf34`](#insn-00b4bf34) 範囲 `[['00b4bf34', '00b4bf4b']]`
  - `FALL_THROUGH` [`00b4bf48`](#insn-00b4bf48) → [`00b4bf4c`](#insn-00b4bf4c)
- ブロック [`00b4bf4c`](#insn-00b4bf4c) 範囲 `[['00b4bf4c', '00b4bf5b']]`

## 命令位置別の参照

- [`00b4bebc`](#insn-00b4bebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bec0`](#insn-00b4bec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bec4`](#insn-00b4bec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bed0`](#insn-00b4bed0) → `01125bb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bed4`](#insn-00b4bed4) → [`00b4bf4c`](#insn-00b4bf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bedc`](#insn-00b4bedc) → `01125bc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4bee4`](#insn-00b4bee4) → [`00b4befc`](#insn-00b4befc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bef8`](#insn-00b4bef8) → `01125bc0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b4bf10`](#insn-00b4bf10) → [`00b4bf34`](#insn-00b4bf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bf38`](#insn-00b4bf38) → `01125bb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bf48`](#insn-00b4bf48) → `01125bb8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bf4c`](#insn-00b4bf4c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bf50`](#insn-00b4bf50) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4bebc`](#insn-00b4bebc)

~~~json
{
  "source": "00b4bebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bec0`](#insn-00b4bec0)

~~~json
{
  "source": "00b4bec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bec4`](#insn-00b4bec4)

~~~json
{
  "source": "00b4bec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bed0`](#insn-00b4bed0)

~~~json
{
  "source": "00b4bed0",
  "target": "01125bb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125bb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bed4`](#insn-00b4bed4)

~~~json
{
  "source": "00b4bed4",
  "target": "00b4bf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bedc`](#insn-00b4bedc)

~~~json
{
  "source": "00b4bedc",
  "target": "01125bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125bc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bee4`](#insn-00b4bee4)

~~~json
{
  "source": "00b4bee4",
  "target": "00b4befc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bef8`](#insn-00b4bef8)

~~~json
{
  "source": "00b4bef8",
  "target": "01125bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125bc0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bf10`](#insn-00b4bf10)

~~~json
{
  "source": "00b4bf10",
  "target": "00b4bf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bf38`](#insn-00b4bf38)

~~~json
{
  "source": "00b4bf38",
  "target": "01125bb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125bb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bf48`](#insn-00b4bf48)

~~~json
{
  "source": "00b4bf48",
  "target": "01125bb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125bb8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bf4c`](#insn-00b4bf4c)

~~~json
{
  "source": "00b4bf4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bf50`](#insn-00b4bf50)

~~~json
{
  "source": "00b4bf50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
