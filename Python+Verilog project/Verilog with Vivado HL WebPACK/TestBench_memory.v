`timescale 1ns / 1ps
 module mempy_TB;
 parameter N = 2;
 reg [(2*N) - 1:0] address;
 reg read_en, en;
 wire [(2*N) - 1:0] data;
 
integer i,j;
  
memory_code dut(.address(address),
          .data(data),
          .read_en(read_en),
          .en(en));

initial begin
    address = 0;
    read_en = 0;
    en      = 0;
    #10 $monitor ("address = %h, data = %h, read_en = %b, en = %b", address, data, read_en, en);

    for (i = 0; i < 2**(2*N); i = i + 1 )begin
        for (j = 0; j < 2**(2*N); j = j + 1)begin
            
            #5 address = {i,j};
             read_en = 1;
             en = 1;
             #5 read_en = 0;
             en = 0;
             address = 0;
            
             end
         end
    end
 
 endmodule
