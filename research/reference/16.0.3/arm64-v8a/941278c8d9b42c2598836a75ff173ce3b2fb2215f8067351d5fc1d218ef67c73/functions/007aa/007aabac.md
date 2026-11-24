# 007aabac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `007aa7d0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007aa/007aa7d0.md) · 移動量 `+0x3dc`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0019.md#compare-37151cc8ba3612d87369606030903f8a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007aabac",
  "name": "FUN_007aabac",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a89c6d6e39d1ad8e6a0caa702f76e42ba77e14a8f37b305d7254c79a4bcb61c6",
  "source_text_sha256": "a89c6d6e39d1ad8e6a0caa702f76e42ba77e14a8f37b305d7254c79a4bcb61c6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007aabac",
        "007aac0b"
      ],
      [
        "007aac38",
        "007aac3b"
      ]
    ],
    "bytes_sha256": "5ffb563c2788afb932b77bcfcc18247009c10c3a9ea3a85d9617f5223243028c",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007ac08c](../007ac/007ac08c.md)

## 呼び出し先

- [00aa44c4](../00aa4/00aa44c4.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 440 bytes

~~~c

void FUN_007aabac(undefined8 param_1)

{
  long lVar1;
  ushort local_40 [8];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  local_40[0] = 0;
  FUN_00aa44c4(0x6c,param_1,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007aabac"></a> `007aabac` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-007aabb0"></a> `007aabb0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007aabb4"></a> `007aabb4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007aabb8"></a> `007aabb8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007aabbc"></a> `007aabbc` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007aabc0"></a> `007aabc0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-007aabc4"></a> `007aabc4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-007aabc8"></a> `007aabc8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007aabcc"></a> `007aabcc` | `ff 03 00 79` | strh wzr,[sp] | `FALL_THROUGH`
<a id="insn-007aabd0"></a> `007aabd0` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-007aabd4"></a> `007aabd4` | `80 0d 80 52` | mov w0,#0x6c | `FALL_THROUGH`
<a id="insn-007aabd8"></a> `007aabd8` | `3b e6 0b 94` | bl 0x00aa44c4 | `UNCONDITIONAL_CALL`
<a id="insn-007aabdc"></a> `007aabdc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-007aabe0"></a> `007aabe0` | `68 00 00 36` | tbz w8,#0x0,0x007aabec | `CONDITIONAL_JUMP`
<a id="insn-007aabe4"></a> `007aabe4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aabe8"></a> `007aabe8` | `da b8 12 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-007aabec"></a> `007aabec` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-007aabf0"></a> `007aabf0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007aabf4"></a> `007aabf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007aabf8"></a> `007aabf8` | `01 02 00 54` | b.ne 0x007aac38 | `CONDITIONAL_JUMP`
<a id="insn-007aabfc"></a> `007aabfc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-007aac00"></a> `007aac00` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007aac04"></a> `007aac04` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-007aac08"></a> `007aac08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007aac38"></a> `007aac38` | `d2 b8 12 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007aabac`](#insn-007aabac) 範囲 `[['007aabac', '007aabe3']]`
  - `CONDITIONAL_JUMP` [`007aabe0`](#insn-007aabe0) → [`007aabec`](#insn-007aabec)
  - `FALL_THROUGH` [`007aabe0`](#insn-007aabe0) → [`007aabe4`](#insn-007aabe4)
- ブロック [`007aabe4`](#insn-007aabe4) 範囲 `[['007aabe4', '007aabeb']]`
  - `FALL_THROUGH` [`007aabe8`](#insn-007aabe8) → [`007aabec`](#insn-007aabec)
- ブロック [`007aabec`](#insn-007aabec) 範囲 `[['007aabec', '007aabfb']]`
  - `CONDITIONAL_JUMP` [`007aabf8`](#insn-007aabf8) → [`007aac38`](#insn-007aac38)
  - `FALL_THROUGH` [`007aabf8`](#insn-007aabf8) → [`007aabfc`](#insn-007aabfc)
- ブロック [`007aabfc`](#insn-007aabfc) 範囲 `[['007aabfc', '007aac0b']]`
- ブロック [`007aac38`](#insn-007aac38) 範囲 `[['007aac38', '007aac3b']]`

## 命令位置別の参照

- [`007aabb0`](#insn-007aabb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabb4`](#insn-007aabb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabc8`](#insn-007aabc8) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabcc`](#insn-007aabcc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabd8`](#insn-007aabd8) → [`00aa44c4`](../00aa4/00aa44c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aa44c4` · 推定シンボル `None` · 推定型 `None`
- [`007aabdc`](#insn-007aabdc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabe0`](#insn-007aabe0) → [`007aabec`](#insn-007aabec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabe4`](#insn-007aabe4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabe8`](#insn-007aabe8) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`007aabf0`](#insn-007aabf0) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabf8`](#insn-007aabf8) → [`007aac38`](#insn-007aac38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aabfc`](#insn-007aabfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aac00`](#insn-007aac00) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aac38`](#insn-007aac38) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007aabb0`](#insn-007aabb0)

~~~json
{
  "source": "007aabb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabb4`](#insn-007aabb4)

~~~json
{
  "source": "007aabb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabc8`](#insn-007aabc8)

~~~json
{
  "source": "007aabc8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabcc`](#insn-007aabcc)

~~~json
{
  "source": "007aabcc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabd8`](#insn-007aabd8)

~~~json
{
  "source": "007aabd8",
  "target": "00aa44c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aabdc`](#insn-007aabdc)

~~~json
{
  "source": "007aabdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabe0`](#insn-007aabe0)

~~~json
{
  "source": "007aabe0",
  "target": "007aabec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabe4`](#insn-007aabe4)

~~~json
{
  "source": "007aabe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabe8`](#insn-007aabe8)

~~~json
{
  "source": "007aabe8",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aabf0`](#insn-007aabf0)

~~~json
{
  "source": "007aabf0",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabf8`](#insn-007aabf8)

~~~json
{
  "source": "007aabf8",
  "target": "007aac38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aabfc`](#insn-007aabfc)

~~~json
{
  "source": "007aabfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aac00`](#insn-007aac00)

~~~json
{
  "source": "007aac00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aac38`](#insn-007aac38)

~~~json
{
  "source": "007aac38",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
