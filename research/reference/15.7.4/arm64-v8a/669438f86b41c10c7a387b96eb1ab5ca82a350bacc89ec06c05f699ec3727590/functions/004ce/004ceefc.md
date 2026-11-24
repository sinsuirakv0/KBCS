# 004ceefc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `004ceefc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ceefc.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0003.md#compare-33fc87976df43a40ffd66bdf968c012d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `004f1d94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1d94.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0002.md#compare-64d4609164ddc482cf79de2454feea17)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ceefc",
  "name": "_ZTv0_n48_NK5Botan13RSA_PublicKey10key_lengthEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "92248f85f662ab74872ab39c16b2673522112b2972c0a2769e08f902d35e4057",
  "source_text_sha256": "92248f85f662ab74872ab39c16b2673522112b2972c0a2769e08f902d35e4057",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ceefc",
        "004cef7f"
      ]
    ],
    "bytes_sha256": "1114bf003008e874fe8014b4b27a82578b0ad8269e7739ae97b8be847ecbaaaf",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 899 bytes

~~~c

long _ZTv0_n48_NK5Botan13RSA_PublicKey10key_lengthEv(long *param_1)

{
  long lVar1;
  uint uVar2;
  ulong uVar3;
  ulong uVar4;
  long lVar5;
  
  lVar5 = *(long *)((long)param_1 + *(long *)(*param_1 + -0x30) + 8);
  lVar1 = *(long *)((long)param_1 + *(long *)(*param_1 + -0x30) + 0x10) - lVar5;
  uVar3 = lVar1 >> 2;
  uVar4 = uVar3;
  if (lVar1 == 0) {
LAB_004cef38:
    if (uVar4 != 0) {
      uVar4 = uVar4 - 1;
      if (uVar4 < uVar3) {
        uVar2 = *(uint *)(lVar5 + uVar4 * 4);
      }
      else {
        uVar2 = 0;
      }
      lVar5 = 0x20;
      do {
        if ((uVar2 >> (ulong)((int)lVar5 - 1U & 0x1f) & 1) != 0) break;
        lVar5 = lVar5 + -1;
      } while (lVar5 != 0);
      return lVar5 + uVar4 * 0x20;
    }
  }
  else {
    do {
      if (*(int *)(lVar5 + -4 + uVar4 * 4) != 0) goto LAB_004cef38;
      uVar4 = uVar4 - 1;
    } while (uVar4 != 0);
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ceefc"></a> `004ceefc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004cef00"></a> `004cef00` | `08 01 5d f8` | ldur x8,[x8, #-0x30] | `FALL_THROUGH`
<a id="insn-004cef04"></a> `004cef04` | `09 00 08 8b` | add x9,x0,x8 | `FALL_THROUGH`
<a id="insn-004cef08"></a> `004cef08` | `28 a5 40 a9` | ldp x8,x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-004cef0c"></a> `004cef0c` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004cef10"></a> `004cef10` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004cef14"></a> `004cef14` | `00 01 00 54` | b.eq 0x004cef34 | `CONDITIONAL_JUMP`
<a id="insn-004cef18"></a> `004cef18` | `0b 11 00 d1` | sub x11,x8,#0x4 | `FALL_THROUGH`
<a id="insn-004cef1c"></a> `004cef1c` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-004cef20"></a> `004cef20` | `6c 79 6a b8` | ldr w12,[x11, x10, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004cef24"></a> `004cef24` | `ac 00 00 35` | cbnz w12,0x004cef38 | `CONDITIONAL_JUMP`
<a id="insn-004cef28"></a> `004cef28` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004cef2c"></a> `004cef2c` | `a1 ff ff 54` | b.ne 0x004cef20 | `CONDITIONAL_JUMP`
<a id="insn-004cef30"></a> `004cef30` | `08 00 00 14` | b 0x004cef50 | `UNCONDITIONAL_JUMP`
<a id="insn-004cef34"></a> `004cef34` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-004cef38"></a> `004cef38` | `ca 00 00 b4` | cbz x10,0x004cef50 | `CONDITIONAL_JUMP`
<a id="insn-004cef3c"></a> `004cef3c` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004cef40"></a> `004cef40` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004cef44"></a> `004cef44` | `a9 00 00 54` | b.ls 0x004cef58 | `CONDITIONAL_JUMP`
<a id="insn-004cef48"></a> `004cef48` | `09 79 6a b8` | ldr w9,[x8, x10, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004cef4c"></a> `004cef4c` | `04 00 00 14` | b 0x004cef5c | `UNCONDITIONAL_JUMP`
<a id="insn-004cef50"></a> `004cef50` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-004cef54"></a> `004cef54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004cef58"></a> `004cef58` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-004cef5c"></a> `004cef5c` | `48 e9 7b d3` | lsl x8,x10,#0x5 | `FALL_THROUGH`
<a id="insn-004cef60"></a> `004cef60` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-004cef64"></a> `004cef64` | `4b 05 00 51` | sub w11,w10,#0x1 | `FALL_THROUGH`
<a id="insn-004cef68"></a> `004cef68` | `2b 25 cb 1a` | lsr w11,w9,w11 | `FALL_THROUGH`
<a id="insn-004cef6c"></a> `004cef6c` | `6b 00 00 37` | tbnz w11,#0x0,0x004cef78 | `CONDITIONAL_JUMP`
<a id="insn-004cef70"></a> `004cef70` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004cef74"></a> `004cef74` | `81 ff ff 54` | b.ne 0x004cef64 | `CONDITIONAL_JUMP`
<a id="insn-004cef78"></a> `004cef78` | `40 01 08 8b` | add x0,x10,x8 | `FALL_THROUGH`
<a id="insn-004cef7c"></a> `004cef7c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004ceefc`](#insn-004ceefc) 範囲 `[['004ceefc', '004cef17']]`
  - `CONDITIONAL_JUMP` [`004cef14`](#insn-004cef14) → [`004cef34`](#insn-004cef34)
  - `FALL_THROUGH` [`004cef14`](#insn-004cef14) → [`004cef18`](#insn-004cef18)
- ブロック [`004cef18`](#insn-004cef18) 範囲 `[['004cef18', '004cef1f']]`
  - `FALL_THROUGH` [`004cef1c`](#insn-004cef1c) → [`004cef20`](#insn-004cef20)
- ブロック [`004cef20`](#insn-004cef20) 範囲 `[['004cef20', '004cef27']]`
  - `CONDITIONAL_JUMP` [`004cef24`](#insn-004cef24) → [`004cef38`](#insn-004cef38)
  - `FALL_THROUGH` [`004cef24`](#insn-004cef24) → [`004cef28`](#insn-004cef28)
- ブロック [`004cef28`](#insn-004cef28) 範囲 `[['004cef28', '004cef2f']]`
  - `CONDITIONAL_JUMP` [`004cef2c`](#insn-004cef2c) → [`004cef20`](#insn-004cef20)
  - `FALL_THROUGH` [`004cef2c`](#insn-004cef2c) → [`004cef30`](#insn-004cef30)
- ブロック [`004cef30`](#insn-004cef30) 範囲 `[['004cef30', '004cef33']]`
  - `UNCONDITIONAL_JUMP` [`004cef30`](#insn-004cef30) → [`004cef50`](#insn-004cef50)
- ブロック [`004cef34`](#insn-004cef34) 範囲 `[['004cef34', '004cef37']]`
  - `FALL_THROUGH` [`004cef34`](#insn-004cef34) → [`004cef38`](#insn-004cef38)
- ブロック [`004cef38`](#insn-004cef38) 範囲 `[['004cef38', '004cef3b']]`
  - `CONDITIONAL_JUMP` [`004cef38`](#insn-004cef38) → [`004cef50`](#insn-004cef50)
  - `FALL_THROUGH` [`004cef38`](#insn-004cef38) → [`004cef3c`](#insn-004cef3c)
- ブロック [`004cef3c`](#insn-004cef3c) 範囲 `[['004cef3c', '004cef47']]`
  - `CONDITIONAL_JUMP` [`004cef44`](#insn-004cef44) → [`004cef58`](#insn-004cef58)
  - `FALL_THROUGH` [`004cef44`](#insn-004cef44) → [`004cef48`](#insn-004cef48)
- ブロック [`004cef48`](#insn-004cef48) 範囲 `[['004cef48', '004cef4f']]`
  - `UNCONDITIONAL_JUMP` [`004cef4c`](#insn-004cef4c) → [`004cef5c`](#insn-004cef5c)
- ブロック [`004cef50`](#insn-004cef50) 範囲 `[['004cef50', '004cef57']]`
- ブロック [`004cef58`](#insn-004cef58) 範囲 `[['004cef58', '004cef5b']]`
  - `FALL_THROUGH` [`004cef58`](#insn-004cef58) → [`004cef5c`](#insn-004cef5c)
- ブロック [`004cef5c`](#insn-004cef5c) 範囲 `[['004cef5c', '004cef63']]`
  - `FALL_THROUGH` [`004cef60`](#insn-004cef60) → [`004cef64`](#insn-004cef64)
- ブロック [`004cef64`](#insn-004cef64) 範囲 `[['004cef64', '004cef6f']]`
  - `CONDITIONAL_JUMP` [`004cef6c`](#insn-004cef6c) → [`004cef78`](#insn-004cef78)
  - `FALL_THROUGH` [`004cef6c`](#insn-004cef6c) → [`004cef70`](#insn-004cef70)
- ブロック [`004cef70`](#insn-004cef70) 範囲 `[['004cef70', '004cef77']]`
  - `CONDITIONAL_JUMP` [`004cef74`](#insn-004cef74) → [`004cef64`](#insn-004cef64)
  - `FALL_THROUGH` [`004cef74`](#insn-004cef74) → [`004cef78`](#insn-004cef78)
- ブロック [`004cef78`](#insn-004cef78) 範囲 `[['004cef78', '004cef7f']]`

## 命令位置別の参照

- [`004cef14`](#insn-004cef14) → [`004cef34`](#insn-004cef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef24`](#insn-004cef24) → [`004cef38`](#insn-004cef38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef2c`](#insn-004cef2c) → [`004cef20`](#insn-004cef20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef30`](#insn-004cef30) → [`004cef50`](#insn-004cef50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef38`](#insn-004cef38) → [`004cef50`](#insn-004cef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef44`](#insn-004cef44) → [`004cef58`](#insn-004cef58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef4c`](#insn-004cef4c) → [`004cef5c`](#insn-004cef5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef6c`](#insn-004cef6c) → [`004cef78`](#insn-004cef78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004cef74`](#insn-004cef74) → [`004cef64`](#insn-004cef64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004cef14`](#insn-004cef14)

~~~json
{
  "source": "004cef14",
  "target": "004cef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef24`](#insn-004cef24)

~~~json
{
  "source": "004cef24",
  "target": "004cef38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef2c`](#insn-004cef2c)

~~~json
{
  "source": "004cef2c",
  "target": "004cef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef30`](#insn-004cef30)

~~~json
{
  "source": "004cef30",
  "target": "004cef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef38`](#insn-004cef38)

~~~json
{
  "source": "004cef38",
  "target": "004cef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef44`](#insn-004cef44)

~~~json
{
  "source": "004cef44",
  "target": "004cef58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef4c`](#insn-004cef4c)

~~~json
{
  "source": "004cef4c",
  "target": "004cef5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef6c`](#insn-004cef6c)

~~~json
{
  "source": "004cef6c",
  "target": "004cef78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004cef74`](#insn-004cef74)

~~~json
{
  "source": "004cef74",
  "target": "004cef64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
