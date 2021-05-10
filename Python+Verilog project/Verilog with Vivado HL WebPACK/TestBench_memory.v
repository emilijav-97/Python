module memory_python_tb();
	parameter N = 4;
	reg [N -1:0] address;
	reg read_enable;
	wire [N -1:0] data;
	integer i;

	memory_python #(N) inst( .read_en(read_en),
				 .data(data), 
				 .address(address, 
				 .read_enable(read_enable));
 
initial begin
	address = 0;
   	read_en = 0;
   	#10 $monitor ("address = %b, data = %b, read_enable = %b", address, data, read_enable);
   
	for (i = 0; i <(2**n); i = i +1)
		begin
			read_enable = 0;
     			#10 address = i;
     			read_enable = 1;
   		end
end
endmodule
